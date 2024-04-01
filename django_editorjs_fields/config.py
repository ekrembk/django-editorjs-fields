from secrets import token_urlsafe

from django.conf import settings
from django.urls import reverse_lazy

DEBUG = getattr(settings, "DEBUG", False)

VERSION = getattr(settings, "EDITORJS_VERSION", '2.29.1')

# ATTACHMENT_REQUIRE_AUTHENTICATION = str(
#     getattr(settings, "EDITORJS_ATTACHMENT_REQUIRE_AUTHENTICATION", True)
# )

EMBED_HOSTNAME_ALLOWED = str(
    getattr(settings, "EDITORJS_EMBED_HOSTNAME_ALLOWED", (
        'player.vimeo.com',
        'www.youtube.com',
        'coub.com',
        'vine.co',
        'imgur.com',
        'gfycat.com',
        'player.twitch.tv',
        'player.twitch.tv',
        'music.yandex.ru',
        'codepen.io',
        'www.instagram.com',
        'twitframe.com',
        'assets.pinterest.com',
        'www.facebook.com',
        'www.aparat.com',
    ))
)

IMAGE_UPLOAD_PATH = str(
    getattr(settings, "EDITORJS_IMAGE_UPLOAD_PATH", 'uploads/images/')
)

IMAGE_UPLOAD_PATH_DATE = getattr(
    settings, "EDITORJS_IMAGE_UPLOAD_PATH_DATE", '%Y/%m/')

IMAGE_NAME_ORIGINAL = getattr(
    settings, "EDITORJS_IMAGE_NAME_ORIGINAL", False)

IMAGE_NAME = getattr(
    settings, "EDITORJS_IMAGE_NAME", lambda **_: token_urlsafe(8))

PLUGINS = getattr(
    settings, "EDITORJS_DEFAULT_PLUGINS", (
        '@editorjs/paragraph@2.11.4',
        '@editorjs/image@2.9.0',
        '@editorjs/header@2.8.1',
        '@editorjs/list@1.9.0',
        '@editorjs/checklist@1.6.0',
        '@editorjs/quote@2.6.0',
        '@editorjs/raw@2.5.0',
        '@editorjs/code@2.9.0',
        '@editorjs/inline-code@1.5.0',
        '@editorjs/embed@2.7.0',
        '@editorjs/delimiter@1.4.0',
        '@editorjs/warning@1.4.0',
        '@editorjs/marker@1.4.0',
        '@editorjs/table@2.3.0',
        '@editorjs/link@2.6.2',
    )
)

CONFIG_TOOLS = getattr(
    settings, "EDITORJS_DEFAULT_CONFIG_TOOLS", {
        'Image': {
            'class': 'ImageTool',
            'inlineToolbar': True,
            "config": {
                "endpoints": {
                    "byFile": reverse_lazy('editorjs_image_upload'),
                    "byUrl": reverse_lazy('editorjs_image_by_url')
                }
            },
        },
        'Header': {
            'class': 'Header',
            'inlineToolbar': True,
            'config': {
                'placeholder': 'Enter a header',
                'levels': [2, 3, 4],
                'defaultLevel': 2,
            }
        },
        'Checklist': {'class': 'Checklist', 'inlineToolbar': True},
        'List': {'class': 'List', 'inlineToolbar': True},
        'Quote': {'class': 'Quote', 'inlineToolbar': True},
        'Raw': {'class': 'RawTool'},
        'Code': {'class': 'CodeTool'},
        'InlineCode': {'class': 'InlineCode'},
        'Embed': {'class': 'Embed'},
        'Delimiter': {'class': 'Delimiter'},
        'Warning': {'class': 'Warning', 'inlineToolbar': True},
        'LinkTool': {
            'class': 'LinkTool',
            'config': {
                # Backend endpoint for url data fetching
                'endpoint': reverse_lazy('editorjs_linktool'),
            }
        },
        'Marker': {'class': 'Marker', 'inlineToolbar': True},
        'Table': {'class': 'Table', 'inlineToolbar': True},
    }
)

PLUGINS_KEYS = {
    '@editorjs/image': 'Image',
    '@editorjs/header': 'Header',
    '@editorjs/checklist': 'Checklist',
    '@editorjs/list': 'List',
    '@editorjs/quote': 'Quote',
    '@editorjs/raw': 'Raw',
    '@editorjs/code': 'Code',
    '@editorjs/inline-code': 'InlineCode',
    '@editorjs/embed': 'Embed',
    '@editorjs/delimiter': 'Delimiter',
    '@editorjs/warning': 'Warning',
    '@editorjs/link': 'LinkTool',
    '@editorjs/marker': 'Marker',
    '@editorjs/table': 'Table',
}
