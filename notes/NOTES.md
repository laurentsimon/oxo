## Installation

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install pip-tools
echo "ostorlab==1.0.30" > notes/install/requirements.in
pip-compile --generate-hashes --output-file=notes/install/requirements.txt --strip-extras notes/install/requirements.in
pip3 install --require-hashes -r notes/install/requirements.txt 
```