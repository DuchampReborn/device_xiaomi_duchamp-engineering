#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/duchamp-engineering',
    'vendor/xiaomi/duchamp-engineering'
]

def lib_fixup_system_ext_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}-{partition}' if partition == 'system_ext' else None


lib_fixups: lib_fixups_user_type = {

}

blob_fixups: blob_fixups_user_type = {
   
 ('system_ext/lib64/libem_audio_jni.so',
     'system_ext/lib64/libaudiotoolkit.so'): blob_fixup()
        .add_needed('libaudioclient_mt6897.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'duchamp-engineering',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
