#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

PRODUCT_PACKAGES += \
    libaudioclient_mt6897

# Inherit from the proprietary version
$(call inherit-product, vendor/xiaomi/duchamp-engineering/duchamp-engineering-vendor.mk)
