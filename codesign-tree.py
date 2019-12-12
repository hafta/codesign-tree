# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/. */

"""Runs the macOS codesign(1) command on a directory tree

This script runs the codesign(1) command on a directory tree as
specified by a provided JSON mappings file referred to as a map file.
The function codesign_tree does the bulk of the work and is written
to be reused when the code is included as a module. The format of the
JSON map file is as follows.

Each entry in the json["map"] array corresponds to one invocation of
the codesign command optionally using the "--deep", "--option runtime",
and "--entitlement <file>" CLI arguments. The files to be codesigned
are the files matching any of the glob patterns.

    {
        "map" : [
        {
          "deep"         : <boolean>,
          "runtime"      : <boolean>,
          "entitlements" : [<one or zero entitlement filenames all
                            from the same directory>],
          "globs"        : [<one or more glob filename patterns
                            relative to a root directory provided
                            to the script>]
        }
        {
          "deep"         : <boolean>,
          "runtime"      : <boolean>,
          "entitlements" : [<...>],
          "globs"        : [<...>, <...>, <...>, ...]
        }
        ...
        ]
    }

For example,

    {
        "map" : [
        {
          "deep"         : false,
          "runtime"      : true,
          "entitlements" : [default.xml],
          "globs"        : [
            "/Contents/MacOS/XUL",
            "/Contents/MacOS/pingsender",
            "/Contents/MacOS/minidump-analyzer",
            "/Contents/MacOS/*.dylib"
          ]
        }
    }

Note:

  1) Each "map" array entry represents one invocation of the codesign
     command which is executed preserving the order of the input file
     and includes all files matching all the glob patterns from the
     "globs" entry.
  2) The entitlements array must either be empty or contain a single
     filename for an entitlements file contained in the entitlements
     directory passed to the script.
  3) The globs array must contain one or more filename glob patterns
     which must each start with a "/" representing the root directory
     The files matching each glob entry are input to the codesign
     command in order.

"""

import argparse
import glob
import json
import logging
import os
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", action="store_true",
            help="print information about arguments and the codesign " +
            "commands to be executed", default=False)

    parser.add_argument("-n", "--simulate", action="store_true",
            help="don't do anything, just print codesign commands")

    parser.add_argument("-m", "--map-file", type=str, required=True,
            help="the JSON codesigning map file path")

    parser.add_argument("-d", "--ent-dir", type=str, required=True,
            help="the entitlement file directory")

    parser.add_argument("-r", "--root-dir", type=str, required=True,
            help="the root dir, e.g., /Users/me/MyApp.app")

    parser.add_argument("-s", "--sign", type=str, required=True,
            help="the codesigning identity to use")

    args = parser.parse_args()

    logger = logging.getLogger('codesign')
    logger.setLevel(logging.DEBUG)

    # check map file
    if not os.path.exists(args.map_file):
        logger.error("Invalid map file: \"%s\"" % args.map_file)
        sys.exit(-1)
    if not os.access(args.map_file, os.R_OK):
        logger.error("Map file read access error:\"%s\"" % args.map_file)
        sys.exit(-1)
    map_file = os.path.realpath(args.map_file)

    # check entitlement dir
    if not os.path.isdir(args.ent_dir):
        logger.error("Invalid entitlements directory: \"%s\"" % (args.ent_dir))
        sys.exit(-1)
    ent_dir = os.path.realpath(args.ent_dir)
    ent_dir = ent_dir.rstrip("/")

    # check root dir
    if not os.path.isdir(args.root_dir):
        logger.error("Invalid root directory: \"%s\"" % (args.root_dir))
        sys.exit(-1)
    root_dir = os.path.realpath(args.root_dir)
    root_dir = root_dir.rstrip("/")

    if args.verbose:
        print("JSON map file:          %s" % map_file);
        print("Entitlement directory:  %s" % ent_dir);
        print("Root directory:         %s" % root_dir);
        print("Codesigning identity:   %s" % args.sign);

    exit_code = 0
    if not codesign_tree(map_file, root_dir, ent_dir, args.sign,
            args.simulate, args.verbose, logger):
        exit_code = -1

    sys.exit(exit_code)

def codesign_tree(map_file,
        root_dir,
        ent_dir,
        cs_id,
        simulate,
        verbose,
        log,
        cs_path="/usr/bin/codesign"):

    """Codesign a tree of files

    Given a map file and a directory tree rooted at the provided root
    dir, run the codesign command on the files specified.

    Returns False if an error was encountered, otherwise True.

    Parameters:
    map_file (string) -- path to the the JSON map file as documented
                         above
    root_dir (string) -- path to the root directory
    ent_dir (string)  -- path to the directory containing any
                         entitlement files used in the map file
    cs_id (string)    -- the codesigning identity to use for the
                         codesign command
    simulate (bool)   -- a flag indicating the codesign command should
                         not be run
    verbose (bool)    -- a flag for printing extra information
    log (logger)      -- a logger to use for logging errors, warnings
    cs_path (string)  -- path to the codesign command
                         (default "/usr/bin/codesign")
    """

    MIN_PYTHON = (3, 5) # due to the use of glob recursive option
    if sys.version_info < MIN_PYTHON:
        log.error("ERROR: Python %s.%s or later is required." % MIN_PYTHON)
        return False

    ent_dir = ent_dir.rstrip("/")
    root_dir = root_dir.rstrip("/")

    log.debug("json map file: %s" % map_file);
    log.debug("entitlement directory: %s" % map_file);
    log.debug("root directory: %s" % root_dir);
    log.debug("codesigning identity: %s" % cs_id);
    log.debug("codesign command to use: %s" % cs_path);

    cs_map_string = open(map_file).read()
    cs_map = json.loads(cs_map_string)

    for cs_entry in cs_map["map"]:
        if "deep" not in cs_entry:
            log.error("\"deep\" key missing from map entry");
            return False
        if "runtime" not in cs_entry:
            log.error("\"runtime\" key missing from map entry");
            return False
        if "entitlements" not in cs_entry:
            log.error("\"entitlements\" key missing from map entry");
            return False
        if "globs" not in cs_entry:
            log.error("\"globs\" key missing from map entry");
            return False

    # Walk the map and make sure all referenced entitlement files are
    # present and readable. Log a warning if filename glob patterns
    # don't match any files.
    for cs_entry in cs_map["map"]:
        if len(cs_entry["entitlements"]) is 1:
            ent_filename = cs_entry["entitlements"][0]
            ent_fullpath = ent_dir + "/" + ent_filename;
            if (not os.path.exists(ent_fullpath) or
                    not os.access(ent_fullpath, os.R_OK)):
                log.error("entitlement file \"%s\" could not be read" %
                        ent_fullpath)
                return False
        if len(cs_entry["entitlements"]) > 1:
            log.error("more than one entitlement file specified for a " +
                    "single codesign map entry")
            return False
        for path_glob in cs_entry["globs"]:
            if not path_glob.startswith("/"):
                log.error("file pattern \"%s\" must start with \"/\""
                        % path_glob)
                return False
            binary_paths = glob.glob(root_dir + path_glob, recursive=True)
            if len(binary_paths) is 0:
                log.warning("file pattern \"%s\" matches no files" % path_glob)

    # walk the map and run codesign for each entry
    for cs_entry in cs_map["map"]:
        cs_cmd = [cs_path, "--force", "-v", "--sign", cs_id]
        if "deep" in cs_entry:
            cs_cmd.append("--deep")
        if "runtime" in cs_entry:
            cs_cmd.append("--options")
            cs_cmd.append("runtime")
        if len(cs_entry["entitlements"]) > 0:
            ent_fullpath = ent_dir + "/" + cs_entry["entitlements"][0]
            cs_cmd.append("--entitlements")
            cs_cmd.append(ent_fullpath)
        for path_glob in cs_entry["globs"]:
            path_glob = root_dir + path_glob
            binary_paths = glob.glob(path_glob, recursive=True)
            for binary_path in binary_paths:
                cs_cmd.append(binary_path)
        if verbose or simulate:
            log.info(" ".join(cs_cmd))
            print(" ".join(cs_cmd))
        if not simulate:
            subprocess.run(cs_cmd)

    return True

if __name__ == '__main__':
    main()
