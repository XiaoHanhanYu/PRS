# -*- mode: python ; coding: utf-8 -*-
# -*- mode: python -*-
import os
p = ['E:\\Pattern_Recognition\\src\\', 'E:\\Pattern_Recognition\\src\\blazeface\\', 'E:\\Pattern_Recognition\\src\\ui\\']
pyfiles = [r'E:\Pattern_Recognition\main.py']
for pi in p:
  for fn in os.listdir(pi):
    if fn.split('.')[-1] == 'py':
      pyfiles.append(pi + fn)


a = Analysis(
    pyfiles,
    pathex=['E:\Pattern_Recognition'],
    binaries=[('E:\\Pattern_Recognition\\src\\__pycache__\\config.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\data.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\Gabor.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\model.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\preprocess.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\recognition.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\recognition_camera.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\recognition_video.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\utils.cpython-38.pyc', 'src\\__pycache__'), ('E:\\Pattern_Recognition\\src\\__pycache__\\visualize.cpython-38.pyc', 'src\\__pycache__')],
    datas=[('E:\\Pattern_Recognition\\assets\\*', 'assets'), ('E:\\Pattern_Recognition\\config', '.'), ('E:\\Pattern_Recognition\\data\\*', 'data'), ('E:\\Pattern_Recognition\\dataset\\*', 'dataset'), ('E:\\Pattern_Recognition\\input\\*', 'input'), ('E:\\Pattern_Recognition\\models\\*', 'models'), ('E:\\Pattern_Recognition\\output', 'output'), ('E:\\Pattern_Recognition\\src\\blazeface\\weights\\*', 'src\\blazeface\\weights')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PRS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\logo\\logo.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
