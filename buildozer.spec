[app]

title = AGRICULTURAL BANK ASHMANT

package.name = agriculturalbankashmant
package.domain = org.ashmant.bank

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 3.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True

[buildozer]

log_level = 2

warn_on_root = 1
