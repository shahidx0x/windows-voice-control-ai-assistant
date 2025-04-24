import os
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

# Define paths
# WORKSPACE_PATH = os.path.abspath(os.path.dirname(__file__))
WORKSPACE_PATH = r'c:\Users\x10ge\OneDrive\Desktop\ai-ass'
SYSTEM32_PATH = r'C:\Windows\System32'
PYTHON_PATH = os.path.dirname(sys.executable)

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[WORKSPACE_PATH],
    binaries=[
        (os.path.join(SYSTEM32_PATH, 'vcruntime140.dll'), '.'),  # Updated path
        (os.path.join(SYSTEM32_PATH, 'msvcp140.dll'), '.')       # Updated path
    ],
    datas=[
        ('src', 'src'),
        ('assets', 'assets'),
        ('README.md', '.')
    ],
    hiddenimports=[
        'speech_recognition',
        'pyaudio',
        'numpy',
        'tkinter',
        'tkinter.ttk',
        'tkinter.font',
        'threading',
        'queue',
        'logging'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

# Clean builds
a.binaries = [x for x in a.binaries if not x[0].startswith('api-ms-win')]
a.binaries = [x for x in a.binaries if not x[0].startswith('vcruntime')]

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Windows Voice Controller AI Assistant',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/base.ico',
    version='file_version_info.txt'
)