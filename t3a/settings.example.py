from settings_base import *

ADMINS = (
    ('Yuan Ma', 'yuan@gestalt.io'),
    ('Gene Gurvich', 'gene@gestalt.io'),
    ('Luke Connolly', 'luke@gestalt.io'),
)

# Do not use precompilers in development as CssAbsoluteFilter is not applied in dev
# even though precompilers are ran (https://github.com/jezdez/django_compressor/pull/331)
# Fall back to using less.js in development instead.
DEBUG = True
LESS_PRODUCTION = True

if not DEBUG:
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )


# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False