//File part of geo_distancia.HTML
// Use this file to calculate distances from the study area using forms


// Example on the structure of the stations organization
//  stations.rotterdam = {};
//  stations.rotterdam.coords = {};
//  stations.rotterdam.name = "Rotterdam";
//  stations.rotterdam.code = 06344;
// [stations.rotterdam.coords.latitude,stations.rotterdam.coords.longitude] = (ParseDMS("51� 58' 0' N. 04� 27' 0' E"));

// from http://www.sciamachy-validation.org/climatology/metadata/
//*** 06280 Groningen (Eelde) 53� 07' N.B. 06� 35'O.L.
//*** 06270 Leeuwarden 	53� 13' N.B. 05� 45' O.L.
//*** 06344 Rotterdam 	51� 58' N.B. 04� 27' O.L
//*** 06380 Maastricht 	50� 54' N.B. 05� 46' O.L.
//***06370 Eindhoven  51� 27' N.B. 05� 23' O.L.
//***06260 De Bilt 	52� 06' N.B. 05� 11'O.L.
//06240 Schiphol (Amsterdam)  52�18� 04�46�
//06235 De Kooy (Den Helder)	52� 56' N.B. 04� 47'O.L.
//06290 Twenthe 	52� 16' N.B. 06� 53'O.L.
//06310 Vlissingen 	51� 27' N.B. 03� 36'O.L.

// Creating a new object with the knmi coordinates

var stations = {
	groningen: {
    	coords: {},
    	name: "Groningen",
    	code: "06280",
	},

	leeuwarden: {
    	coords: {},
  		name: "Leeuwarden",
  		code: "06270",
    },

	rotterdam: {
		coords: {},
 		name: "Rotterdam",
		code: "06344",
    },

	maastricht: {
		coords: {},
		name: "Maastricht",
		code: 06380,
    },

    eindhoven: {
		coords: {},
		name: "Eindhoven",
		code: 06370,
    },

    deBilt: {
		coords: {},
		name: "DeBilt",
		code: 06260,
    },

    schiphol: {
		coords: {},
		name: "Schiphol",
		code: 06240,
    },

    deKooy: {
		coords: {},
		name: "DeKooy",
		code: 06235,
    },

    twenthe: {
		coords: {},
		name: "Twenthe",
		code: 06290,
    },

    vlissingen: {
		coords: {},
		name: "Vlissingen",
		code: 06310,
    },
};


// Adding Coordinates:
[stations.groningen.coords.latitude,stations.groningen.coords.longitude] =      (ParseDMS("53� 07' 0' N. 06� 35' 0' E"));
[stations.leeuwarden.coords.latitude,stations.leeuwarden.coords.longitude] =    (ParseDMS("53� 13' 0' N. 05� 46' 0' E"));
[stations.rotterdam.coords.latitude,stations.rotterdam.coords.longitude] =      (ParseDMS("51� 58' 0' N. 04� 27' 0' E"));
[stations.maastricht.coords.latitude,stations.maastricht.coords.longitude] =    (ParseDMS("50� 54' 0' N. 05� 46' 0' E"));
[stations.eindhoven.coords.latitude,stations.eindhoven.coords.longitude] =      (ParseDMS("51� 27' 0' N. 05� 23' 0' E"));
[stations.deBilt.coords.latitude,stations.deBilt.coords.longitude] =            (ParseDMS("52� 06' 0' N. 05� 11' 0' E"));
[stations.schiphol.coords.latitude,stations.schiphol.coords.longitude] =        (ParseDMS("52� 18' 0' N. 04� 46' 0' E"));
[stations.deKooy.coords.latitude,stations.deKooy.coords.longitude] =            (ParseDMS("52� 56' 0' N. 04� 47' 0' E"));
[stations.twenthe.coords.latitude,stations.twenthe.coords.longitude] =          (ParseDMS("52� 16' 0' N. 06� 53' 0' E"));
[stations.vlissingen.coords.latitude,stations.vlissingen.coords.longitude] =    (ParseDMS("51� 27' 0' N. 03� 36' 0' E"));

///////////////////////////////////////////////////////////////////////////////
var map = null;

var ourCoords =  {      // for calculating the distance to CITG-DELFT
	latitude: 51.999033,
	longitude:  4.375638 };

var options = {enableHighaccuracy: true, timeout:0, maximumage:60};
window.onload = getMyLocation;  //run it when the page is loaded

function getMyLocation() {
	if (navigator.geolocation) {    //checks if there is geolocation in the browser

		navigator.geolocation.getCurrentPosition(   //runs the 2 functions below and error
			displayLocation,
			displayError,
			options);
	}
	else {
		alert("Oops, no geolocation support");
	}
}

function displayLocation(position) {    //gets the attributes lat and long and displays it
	var latitude = position.coords.latitude;
	latitude2 = Math.round(latitude * 10000)/10000 //for rounding
	var longitude = position.coords.longitude;
	longitude2 = Math.round(longitude * 10000)/10000

// For the actual position
	var div = document.getElementById("location");

// Displays local position
	div.innerHTML = "Latitude " + latitude2 + ", Longitude " + longitude2;
	div.innerHTML += " (with " + position.coords.accuracy + " meters accuracy)";

// Displays local position
	var div = document.getElementById("time");
	var dateTime = new Date(position.timestamp);
	div.innerHTML = "  Location retrieved on " + dateTime;

// For the distance from the coordinates set in line 4
	var km = computeDistance(position.coords, ourCoords);  //using the code below
	var distance = document.getElementById("distance");
	distance.innerHTML = "You are " + km + " km away from the TU Delft!";

/////////////////////////////////////////////////////////////////////////////////
// For the teste
// To calculate the distance to each point (stations.rotterdam.distance = computeDistance(position.coords, stations.rotterdam.coords))
    function searchDist (obj){
        for (var item in obj){
                stations[item].distance = computeDistance(position.coords, stations[item].coords);
        }
    };

    searchDist(stations);

// To find out the closest station
    var d = [];
    var st = []
        for (var name in stations) {
            d.push (stations[name].distance);
            st.push(stations[name].name);
        };

    var minDistance = Math.min.apply(Math,d);
    var d_index = d.indexOf(minDistance);
    var nameStation = st[d_index]
    <!--alert (nameStation)-->

    var kmKnmi = computeDistance(position.coords, stations.rotterdam.coords);
	var teste = document.getElementById("teste");
	teste.innerHTML = " The closest KNMI station is  " + nameStation
    teste.innerHTML += ", located about "+ minDistance + " km away from the study area! " ;

/////////////////////////////////////////////////////////////////////////////////

}      //keep this!

// -----------------------------------------------------------

// To convert from degrees to decimals
function ConvertDMSToDD(degrees, minutes, seconds, direction) {
    var dd = Number(degrees) + Number(minutes)/60 + Number(seconds)/(60*60);
    if (direction == "S" || direction == "W") { dd = dd * -1; }
    return dd;
}

function ParseDMS(input) {
    var parts = input.split(/[^\d\w]+/);
    var lat = ConvertDMSToDD(parts[0], parts[1], parts[2], parts[3]);
    var lng = ConvertDMSToDD(parts[4], parts[5], parts[6], parts[7]);
    return [lat, lng];
}
// -----------------------------------------------------------
// Uses the Spherical Law of Cosines to find the distance between two lat/long points
function computeDistance(startCoords, destCoords) {
	var startLatRads = degreesToRadians(startCoords.latitude);
	var startLongRads = degreesToRadians(startCoords.longitude);
	var destLatRads = degreesToRadians(destCoords.latitude);
	var destLongRads = degreesToRadians(destCoords.longitude);

	var Radius = 6371; // radius of the Earth in km
	var distance = Math.acos(Math.sin(startLatRads) * Math.sin(destLatRads) +
					Math.cos(startLatRads) * Math.cos(destLatRads) *
					Math.cos(startLongRads - destLongRads)) * Radius;
	distance = Math.round(distance * 1000)/1000
	return distance;
}

function degreesToRadians(degrees) {
	radians = (degrees * Math.PI)/180;
	return radians;
}

//-------------------------------------------------------------------------------
// Error display
function displayError(error) {
	var errorTypes = {
		0: "Unknown error",
		1: "Permission denied",
		2: "Position is not available",
		3: "Request timeout"
	};
	var errorMessage = errorTypes[error.code];
	if (error.code == 0 || error.code == 2) {
		errorMessage = errorMessage + " " + error.message;
	}
	var div = document.getElementById("location");
	div.innerHTML = errorMessage;
}


