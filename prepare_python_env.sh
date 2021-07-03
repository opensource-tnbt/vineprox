VINEPROXENV_DIR="$HOME/vineproxenv"
VINEPROX_DIR="$HOME/anuket/vineprox"
PROXCONF_DIR="/tmp/prox"
echo $VINEPROXENV_DIR

if [ -d "$VINEPROXENV_DIR" ] ; then
    echo "Directory $VINEPROXENV_DIR already exists. Skipping python virtualenv creation."
    exit
fi

(virtualenv "$VINEPROXENV_DIR" --python /usr/bin/python3
source "$VINEPROXENV_DIR"/bin/activate
pip install -U pip
pip install -r requirements.txt
git clone https://gerrit.opnfv.org/gerrit/samplevnf /tmp/samplevnf
cd /tmp/samplevnf/VNFs/DPPD-PROX/helper-scripts/rapid
sed -i 's/format.yaml/\/opt\/prox\/format.yaml/g' rapid_test.py
cp helper.lua $VINEPROX_DIR
mkdir $PROXCONF_DIR
cp format.yaml $PROXCONF_DIR
python setup.py build
python setup.py install
rm -rf /tmp/samplevnf)
