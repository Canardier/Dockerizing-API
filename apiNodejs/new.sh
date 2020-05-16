#!/bin/bash

upper=$2;
upper=`echo ${upper:0:1} | tr  '[a-z]' '[A-Z]'`${upper:1}

if [ $1 = "create" ]
then
    echo "Ok create this sir !"
    touch app/models/$2.model.js;
    touch app/controllers/$2.controller.js;
    touch app/routes/$2.routes.js;

    echo "const sql = require(\"./db.js\");

// constructor
const ${2^} = function($2) {

};

module.exports = ${2^};" > app/models/$2.model.js;
    echo "const $upper = require(\"../models/$2.model.js\");" > app/controllers/$2.controller.js;
    echo "module.exports = app => {
        const $2s = require(\"../controllers/$2.controller.js\");
}" > app/routes/$2.routes.js;
fi

if [ $1 = "delete" ]
then
    echo "Ok delete this sir !"
    rm app/models/$2.model.js;
    rm app/controllers/$2.controller.js;
    rm app/routes/$2.routes.js;
fi