//starting refectoring
app.controller("HomeControllerBeta", function($scope, $state,$routeParams, $http, $filter, leafletData, leafletBoundsHelpers, dataService, authService) {

    $scope.searchTabClicked = function(){
        $state.go('home.search');
        $scope.panelCollapse = false;
        dataService.resetData();
        //dataService.resetFilter();  // based on Jos' requirements of not changing searching criteria for a second search
        initApp();
    };

    $scope.resultTabClicked = function(){
        $scope.panelCollapse = false;
        $scope.tabHighLighted = {search: false, result: false, order: false};
        $scope.tabHighLighted.result = true;
        if ($scope.filter.resultmode.stack){
            if (typeof($scope.framedata) != 'undefined'){
                for (var i = 0; i< $scope.framedata.length; i++){
                    var currentStack = $scope.framedata[i]
                    currentStack['isSelected'] = true;
                }
                $state.go('home.result.stack');
            }
        }else {
            $state.go('home.result.image');
        }
    };

    $scope.orderTabClicked = function(){
        $scope.panelCollapse = false;
        $scope.tabHighLighted = {search: false, result: false, order: false};
        $scope.tabHighLighted.order = true;
        $state.go('home.order');
    };

    var parentScope = $scope.$parent;
    $scope.panelCollapse = false;

    $scope.togglePanel = function(){
        $scope.panelCollapse = !($scope.panelCollapse);
    }

    // Google geocoder for search address tool
    var geocoder = new google.maps.Geocoder();

	var googleGeocoding = function(text, callResponse)
	{
		latLonPattern = /^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$/
		if (latLonPattern.test(text) || text.match(/aoi/i)){
		    geocoder.geocode({address: 'aoi'}, callResponse);
		}else{
		    geocoder.geocode({address: text}, callResponse);
		}

	}

	var filterJSONCall = function(rawjson, b, c)
	{
		var json = {},
			key, loc, disp = [];

		var searchText = this._input.value;
		// if the user search for coordinates in lat,lon
		if (latLonPattern.test(searchText)){
		    var latLon = searchText.split(',');
		    var latitude = parseFloat(latLon[0]);
		    var longitude = parseFloat(latLon[1]);
		    json[searchText] = {lat:latitude, lng:longitude};
		    return json;
		}else if  (searchText.match(/aoi/i)){
            var getRemote = function (remote_url) {
                return $.ajax({
                    type: "GET",
                    url: remote_url,
                    async: false
                }).responseText;
            };

            jsonData = getRemote('/catalogue/history_aoi/');
            jsonData = JSON.parse(jsonData);

            for (var i = 0; i<jsonData.length;i++){
                var data = new L.geoJson();
                data.addData(jsonData[i][0]['selection']);
                var features = data.getLayers();
                var feature = {}
                try {
                        var featureCollection = [];
                        for (var t=0;t<features.length; t++){
                            features[t]['feature']['from'] = 'aoi';
                            featureCollection.push(features[t]['feature']);
                        }

                        feature={'type':'FeatureCollection', 'features': featureCollection};

                        var loc = data.getBounds().getCenter();
                }catch(e){
                    try{
                        var loc = data.getLatLng();
                    }catch(e){
                        var loc = data.getBounds().getCenter();
                    }

                }

                loc['feature'] = feature;
                var timestamp = new Date(jsonData[i][1]);

                json['AOI from: '+ timestamp.toLocaleString()] = loc;

            }
        }

		for(var i in rawjson)
		{
			key = rawjson[i].formatted_address;

			loc = L.latLng( rawjson[i].geometry.location.lat(), rawjson[i].geometry.location.lng() );

			json[ key ]= loc;	//key,value format
		}

		return json;

	}


    function getStyle(comesfrom, name){
            if (comesfrom=="aoi")
                { return {fillColor: 'orange',weight: 2,opacity: 1,color: 'red',dashArray: '3',fillOpacity: 0} }
            else if (comesfrom=="searchresults")
                if (name=='ers')
                    { return {fillColor: 'red',weight: 1,opacity: 0.1,color: 'red',fillOpacity: 0.3} }
                else if (name=='tsx')
                    { return {fillColor: 'green',weight: 1,opacity: 0.1,color: 'green',fillOpacity: 0.3} }
                else if (name=='rsat2')
                    { return {fillColor: 'yellow',weight: 1,opacity: 0.1,color: 'yellow',fillOpacity: 0.3} }
                else if (name=='csk')
                    {return {fillColor: 'cyan',weight: 1,opacity: 0.1,color: 'cyan',fillOpacity: 0.3} }
                else if (name=='env')
                    {return {fillColor: 'blue',weight: 1,opacity: 0.1,color: 'blue',fillOpacity: 0.3} }
                else if (name=='sentinel1')
                    {return {fillColor: '#9933FF',weight: 1,opacity: 0.1,color: '#9933FF',fillOpacity: 0.5} }
                else
                    { return {fillColor: 'black',weight: 1,opacity: 0.1,color: 'black',fillOpacity: 0.3} }
            else
                { return {fillColor: 'grey',weight: 1,opacity: 0.2,color: 'grey',fillOpacity: 0.2} }
    }


    function style(feature){
            subkind=feature.properties.satgroup || 'undefined'
            return getStyle(feature.from, subkind.toLowerCase())
    }


    function initMap(){
        angular.extend($scope, {
            amsterdam: { lat: 52.6, lng: 5.7, zoom: 6 },
            layers: {
                baselayers: {
                    googleTerrain: {
                                name: 'Google Terrain',
                                layerType: 'TERRAIN',
                                type: 'google'
                    },
                    googleHybrid: {
                                name: 'Google Hybrid',
                                layerType: 'HYBRID',
                                type: 'google'
                    },
                    googleRoadmap: {
                                name: 'Google Streets',
                                layerType: 'ROADMAP',
                                type: 'google'
                    },
                    mapbox2: {
                        name: 'Light',
                        type: 'xyz',
                        url: 'https://a.tiles.mapbox.com/v3/{layerId}/{z}/{x}/{y}.png',
                        layerParams: {
                            key: '007b9471b4c74da4a6ec7ff43552b16f',
                            layerId: 'mwschouten.ka65g9el'
                            }
                    },
                },

            },
            controls: {
                    draw: {
                        circle: false,
                        polyline: false,
                    },
                },
            aoi: {},
            defaults:{
                maxZoom: 16,
                minZoom: 3,
                attributionControl: false,
                controls: {
                    layers:{
                        position: 'topright',
                        visible: true,
                        collapsed: true,
                    },
                },
            },
            maxBounds: {
                    northEast: {
                        lat: 90,
                        lng: 180
                    },
                    southWest: {
                        lat: -90,
                        lng: -180
                    }
            }
        });



        leafletData.getMap().then(function(map) {
            // add a scale control
            L.control.scale({
                maxWidth : 150
            }).addTo(map)

            var drawnItems = $scope.controls.edit.featureGroup;
            map.on('draw:created', function (e) {
                if (!$scope.tabHighLighted.search){
                    $scope.searchTabClicked();
                }
                var layer = e.layer;
//                $scope.file = "Select File ZIPed shape, kml, kmz";
                $scope.aoi =  e.layer.toGeoJSON();
                dataService.updateAOI($scope.aoi);
                console.log('New selection');
                $scope.framedata=[];
                $scope.updateMap();
                $scope.newaoi = true;
            });

            // search for address
            var search_cntrol = new L.Control.Search({
                callData: googleGeocoding,
                filterJSON: filterJSONCall,
                text: "Search for Locations...",
                markerLocation: false,
                autoType: true,
                autoCollapse: false,
                collapsed: false,
                circleLocation: true,
                minLength: 2,
                position: 'topleft'
		    });

	        search_cntrol.addTo(map);

	        search_cntrol.on('search_locationfound', function(e) {
                var gjson = {
                        "type": "Feature",
                        "properties": {
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [e.latlng.lng, e.latlng.lat]
                        }
                }
                if (e.text.search('AOI from:') > -1 ){
                    gjson = e.latlng.feature;
                }

                $scope.aoi = gjson;

                dataService.updateAOI($scope.aoi);
                $scope.updateMap();
                $scope.newaoi = true;
                dataService.map.fitBounds(L.geoJson($scope.aoi).getBounds());
            })


            dataService.map = map;
            var styleSelected_once = {
                "color": "white",
                "weight": 3,
                "opacity": 0.6,
                "fillOpacity": 0,
            };

            var styleSelected_always = {
                "color": "black",
                "weight": 4,
                "opacity": 0.8,
                "fillOpacity": 0,
            };

            $scope.selectedFeature_once = L.geoJson([],{style:styleSelected_once}).addTo(map);
            $scope.selectedFeature_always = L.geoJson([], {style:styleSelected_always}).addTo(map);
            // This is for high light the frame in stacks display
            // Todo: before we have a good defination for stacks, don't use it
            if (!angular.equals({},dataService.footprints)){
            dataService.map.fitBounds(L.geoJson(dataService.footprints));
            dataService.map.panBy([1,0]);
        };

        });
    };


    var initApp = function(){

        // Default UI settings
        $scope.tabHighLighted = {search: true, result: false, order: false};
//        $scope.timeFilterHighLighted = {AllTime: true, Year: false, HalfYear: false, Month: false, Week: false};

        $scope.activityMessage = '';
        $scope_index_active = undefined;
        $scope_index_new = undefined;
        $scope.graph = {'width':300};
        $scope.datelim = [];
        $scope.newaoi = false;

        // Filter variables
//        $scope.satsearch = {'ers':false, 'env':false, 'TSX':false, 'rsat2':false, 'csk':false, 'Sentinel1':true};
//        $scope.filter.resultmode = {'stack': false};
        $scope.filter = dataService.getFilter();
        if (typeof($scope.filter.date.from)=='string'){
            $scope.filter.date.from = new Date($scope.filter.date.from)
            $scope.filter.date.till = new Date($scope.filter.date.till)
        }
        $scope.nrImages = {all:0, year:0, halfyear:0, month:0, week:0};

        $scope.aoi =  $scope.filter.aoi;

        if ($scope.aoi) {
            $scope.updateMap()
        }

        if ($scope.selectedFeature_always){
            $scope.selectedFeature_always.clearLayers();
        }

        if ($scope.selectedFeature_once){
            $scope.selectedFeature_once.clearLayers();
        }
    }

    $scope.updateMap = function(){
        // Update the map with the list and the number of minimum acquisition
        var data = {
                type:"FeatureCollection",
                features:[]
        }

        // An all-in filter comes here
        var filteredData = filteringData(data);

        var item = $scope.aoi;
        item.from = 'aoi';
        data.features.push(item);

        angular.extend($scope, {
                geojson: {
                    data: filteredData,
                    style: style,
                    resetStyleOnMouseout: true,
                },
        })
        // Todo: make this out of map because it does not belong to map
        $scope.nrImages = $scope.countDates(filteredData)
    }

    var filteringData = function(data){
        for (var i=0; i< dataService.getData().searchresults.features.length; i++){
            var item = dataService.getData().searchresults.features[i];

            if (item.properties.show&&item.properties.isSelected){
                item.from = 'searchresults';
                data.features.push(item);

                if (dataService.getData().searchresults_once.features.length>0){
                    item = dataService.getData().searchresults_once.features[i];
                    item.from = 'searchresults_once';
                    data.features.push(item);
                }
            }
        }
        return data;
    }

    $scope.$on('dataChanged', function(){
        $scope.framedata = dataService.getData().framedata;
        $scope.displayedCollection = [].concat(dataService.getData().framedata);

        $scope.updateMap();
    });

    $scope.countDates = function(dataSource){

        var today = new Date();

        function new_year(value){

            return today - new Date(value) < 1000*60*60*24*365;
        }
        function new_halfyear(value){ return today - new Date(value) < 1000*60*60*24*182; }
        function new_month(value){ return today - new Date(value) < 1000*60*60*24*31; }
        function new_week(value){ return today - new Date(value) < 1000*60*60*24*8; }

        var count = {all:0,year:0,halfyear:0,month:0,week:0};

        for (var i=0;i< dataSource.features.length;i++){
            var item = dataSource.features[i];
            if (item.from == 'searchresults' || typeof(item.from)=='undefined'){
                count.all +=  item.properties.dates.length;
                count.year +=  item.properties.dates.filter(new_year).length;
                count.halfyear +=  item.properties.dates.filter(new_halfyear).length;
                count.month +=  item.properties.dates.filter(new_month).length;
                count.week +=  item.properties.dates.filter(new_week).length;
            }
        }
        return count;
    }

    $scope.showResultTab = function(){
//        var tabShow = (!($scope.framedata.length==0) || ($scope.showFilter == true) || $scope.showResult == true);
        var framedataLength = 0;
        if (typeof(dataService.getData().framedata) != 'undefined'){
            framedataLength = dataService.getData().framedata.length;
        }
        var tabShow = ( framedataLength >0 );
        return tabShow;
    }

    $scope.showOrderTab = function(){
        // Only show order tab when there is result to show
        if ($scope.showResultTab()){
            if (dataService.getData().searchresults.features[0].properties.mode != 'preview'){
                return true
            }
        }else{
            return false
        }
    }

    $scope.searchAgain = function(){
        $scope.newaoi = true;
    }


    initMap();
    initApp();


});