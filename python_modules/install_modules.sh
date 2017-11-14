#!/bin/bash


dir=$(pwd)


echo "export PYTHONPATH=\${PYTHONPATH}:${dir}" >> ~/.zshrc

echo "export JUPYTER_PATH=${dir}:\$JUPYTER_PATH" >> ~/.zshrc
echo "export JUPYTER_PATH=${dir}:\$JUPYTER_PATH" >> ~/.bashrc

