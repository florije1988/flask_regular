/**
 * Created by florije on 2014/12/15.
 */

//(function () {
//
//    'use strict';
//
//    angular.module('TodoApp', [])
//        .run(function($rootScope){
//            $rootScope.hello = 'fuboqing';
//        })
//}());

var app = angular.module('myApp', []);

app.run(function ($rootScope) {
    $rootScope.name = "florije"
});