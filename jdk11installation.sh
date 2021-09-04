#!/bin/bash
#jdk installation
# aug created on 
INSDIR=/home/vagrant
cd $INSDIR
JDKINSTALLER=/vagrant/jdk-11.0.12_linux-x64_bin.tar.gz
if test -f "$JdkINSTALLER"; then
    echo "$JDKINSTALLER exists. "
    [ java -version -ew "11.0.12" ]
    [ ! -d $INSDIR/jdk-11.0.12 ] && tar -xzvf &JdkINSTALLER
  export JAVA_HOME=$INSDIR/jdk-11.0.12/
  export PATH=$JAVA_HOME/bin:$PATH
  java -version
  else
       echo "jdk JdkINSTALLER not found"
fi

