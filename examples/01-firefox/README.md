This example uses a map file that specifies different entitlement files
for the Firefox browser process and plugin-container executable.

This allows us to set allow-dyld-environment-variables=false in the parent
process preventing DYLD_INSERT_LIBRARIES from being used to inject libraries
into Firefox when it is signed with hardened runtime enabled.

TODO: simplify the map file further. We shouldn't have to explicitly sign
/Contents/MacOS/firefox because signing of the Firefox.app bundle should
cover that.

The map file uses `deep` when signing the inner .app bundles. This should
not be necessary because the inner bundles don't include supporting frameworks
or plugins. TODO: decide if this should be changed.
