conda create -n PRS python=3.8.19 -y
conda activate PRS
conda install cudatoolkit=10.1
conda install cudnn=7.6.5
pip install -r requirements.txt
pip install .\dlib-19.19.0-cp38-cp38-win_amd64.whl
pause
