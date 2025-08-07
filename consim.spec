# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

# Get the current directory
current_dir = Path(SPECPATH)

# Define data files to include
static_files = []

# Add all static files (HTML, CSS, JS)
static_dir = current_dir / 'static'
if static_dir.exists():
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            file_path = Path(root) / file
            # Calculate relative path from project root
            rel_path = file_path.relative_to(current_dir)
            # Add as (source, destination_in_bundle)
            static_files.append((str(file_path), str(rel_path.parent)))

# Add source files
src_files = []
src_dir = current_dir / 'src'
if src_dir.exists():
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                rel_path = file_path.relative_to(current_dir)
                src_files.append((str(file_path), str(rel_path.parent)))

a = Analysis(
    ['consim_launcher.py'],
    pathex=[str(current_dir)],
    binaries=[],
    datas=static_files + src_files,
    hiddenimports=[
        'src.lattice_demo',
        'http.server',
        'socketserver',
        'webbrowser',
        'threading',
        'json',
        'urllib.parse'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'numpy',
        'torch',
        'fastapi',
        'uvicorn',
        'websockets',
        'pydantic',
        'multipart',
        'aiofiles'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CONSIM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None
)