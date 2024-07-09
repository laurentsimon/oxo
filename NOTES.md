## Installation

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install pip-tools
echo "ostorlab==1.0.30" > requirements.in
pip-compile --generate-hashes --output-file=requirements.txt --strip-extras requirements.in
```