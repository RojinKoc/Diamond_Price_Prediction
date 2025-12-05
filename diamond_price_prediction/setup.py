from setuptools import setup

APP = ['elmas_tahmin_tkinter.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': None,
    'packages': ['joblib', 'numpy'],
    'includes': ['tkinter'],
    'excludes': ['matplotlib'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

