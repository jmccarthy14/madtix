MYSQL_VER=mysql-5.6.11
MYSQL_DB=tix
HOME_DIR=~
DOWNLOAD_DIR=$HOME_DIR/_tmp_tix_dep_downloads
VE_DIR=$HOME_DIR/tixVE

CUR_DIR=`pwd`
cd ../
PROJECT_DIR=`pwd`
cd $CUR_DIR

function check_deps() {

	if [ -z `which mysql` ]
	then
		echo "ERROR: MySQL is not installed. Please install $MYSQL_VER first and make sure it's in your path."
		exit -1
	fi

	if [ -z `which nginx` ]
	then
		echo "ERROR: nginx is not installed. Please install nginx first and make sure it's in your path."
		exit -1
	fi

	if [[ "$VIRTUAL_ENV" != "" ]]
	then
		echo "ERROR: This script cannot be run from within a virtual env. Please deactivate first."
		exit -1
	fi
}

function get_settings() {
	
	echo "What directory do you want your virtual environment? (default: $HOME_DIR/tixVE): "
	read VE_DIR

	if [ -z $VE_DIR ]
	then 
		VE_DIR="$HOME_DIR/tixVE"
	fi

	#if [ -d "$VE_DIR" ]; then
	# 	echo "ERROR: "$VE_DIR" already exists"
	# 	exit -1
	#fi

}


function prompt_user() {
	echo "------- SETTINGS --------"
	echo "Using:"
	echo "HOME_DIR = $HOME_DIR"
	echo "DOWNLOAD_DIR = $DOWNLOAD_DIR"
	echo "VE_DIR = $VE_DIR"
	echo "PROJECT_DIR = $PROJECT_DIR"
	echo "--------------------------"
	echo "Continue? (y/n): "
	read DO_CONTINUE

	if [$DO_CONTINUE != "y"]
	then
		echo "Aborting..."
	fi
}

function do_setup() {
	#create tmp dl dir
	mkdir $DOWNLOAD_DIR
}

function install_pip() {
	#setup pip globally
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Installing pip globally..."
	echo "---------------------------"
	cd $DOWNLOAD_DIR
	curl -O https://pypi.python.org/packages/source/p/pip/pip-1.3.1.tar.gz $DOWNLOAD_DIR
	tar -xvf pip-1.3.1.tar.gz
	cd pip-1.3.1
	sudo python setup.py install
	cd ../../
	echo "---------------------------"
	echo "pip installation complete!"
	echo "---------------------------"
	echo "--"
	echo "--"
	echo "--"
	echo "--"
}

function install_virtual_env() {
	#setup virtual env
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Setting up a virtual environment..."
	echo "---------------------------"
	cd $DOWNLOAD_DIR
	curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz $DOWNLOAD_DIR
	tar -xvf virtualenv-1.9.1.tar.gz
	cd virtualenv-1.9.1
	python virtualenv.py $VE_DIR
	cd ../../

	if [ -z `cat $HOME_DIR/.bash_profile | grep "source $VE_DIR/bin/activate"` ] 
	then
		echo "Adding Virtual Environment activation to your .bash_profile..."
		echo "source $VE_DIR/bin/activate" >> $HOME_DIR/.bash_profile
		echo "DONE!"
	else
		echo "Sweet, Virtual Environment activation already exists in your .bash_profile!"
	fi

	# go into VE
	source $VE_DIR/bin/activate

	echo "---------------------------"
	echo "Virtual environment setup complete!"
	echo "---------------------------"
	echo "--"
	echo "--"
	echo "--"
	echo "--"
}


function install_distribute() {
	#setup distribute
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Installing distribute into virtual env..."
	echo "---------------------------"
	curl http://python-distribute.org/distribute_setup.py | python
	echo "---------------------------"
	echo "distribute installation complete!"
	echo "---------------------------"
	echo "--"
	echo "--"
	echo "--"
}


function install_web_project_deps() {
	# install deps
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Installing python deps..."
	echo "---------------------------"
	cd $PROJECT_DIR
	pip install -r requirements.txt
	cd $CUR_DIR
	echo "---------------------------"
	echo "python deps installed!"
	echo "---------------------------"
	echo "--"
	echo "--"
	echo "--"
}

function setup_mysql() {
	# run sql scripts
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Building MySQL DB..."
	echo "---------------------------"
	CUR_DIR=`pwd ./`
	cd $PROJECT_DIR
	mysql -uroot -e "CREATE DATABASE $MYSQL_DB"
	python ./manage.py syncdb
	cd $CUR_DIR
	echo "---------------------------"
	echo "python deps installed!"
	echo "---------------------------"
	echo "--"
	echo "--"
	echo "--"
}

function do_cleanup() {
	echo "--"
	echo "--"
	echo "--"
	echo "---------------------------"
	echo "Cleaning up..."
	echo "---------------------------"

	#delete tmp dir
	sudo rm -rf $DOWNLOAD_DIR

	echo "--"
	echo "--"
	echo "--"
	echo "--"
}

function start_app() {
	if [ -z `ps aux | grep "nginx" | grep "worker process"` ]
	then
		echo "nginx is not running. Start nginx first before running the app."
	else
		ps aux | grep python | grep "port=8080" | awk '{print $2}' | xargs kill; python $PROJECT_DIR/manage.py runfcgi host=127.0.0.1 port=8080

		echo "Application should be running at http://localhost If not, make sure nginx is configured to delegate requests to flup."
	fi
}

function finish() {
	echo "Done!"
}


check_deps
get_settings
prompt_user
do_setup
install_pip
install_virtual_env
install_distribute
install_web_project_deps
setup_mysql
do_cleanup
start_app
finish
