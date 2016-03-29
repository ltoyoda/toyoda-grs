//File part of geo_input.HTML
// Use this file to calculate distances from the study area using forms

var map = null;
var ourCoords =  {      // for calculating the distance to CITG-DELFT
	latitude: 51.999033,
	longitude:  4.375638
};

var options = {enableHighaccuracy: true, timeout:0, maximumage:6};

//window.onload = getMyLocation;  //run it when the page is loaded //

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
	var km = computeDistance(position.coords, ourCoords);  //using the code below
	var distance = document.getElementById("distance");

// Displays local position
	div.innerHTML = "You are currently at Latitude: " + latitude2 + ", Longitude: " + longitude2;
	div.innerHTML += " (with " + position.coords.accuracy + " meters accuracy).";
	div.innerHTML += " Just " + km + " km away from the TU Delft!";

	var div = document.getElementById("time");
	var dateTime = new Date(position.timestamp);
// Displays local position
	div.innerHTML = "Position not updated on map. Retrieved on " + dateTime;

// For the distance from the coordinates set in line 4
//	var km = computeDistance(position.coords, ourCoords);  //using the code below
//	var distance = document.getElementById("distance");
// and displays the distance
//	distance.innerHTML = "You are " + km + " km away from the TU Delft";
}
// -----------------------------------------------------------
// Uses the Spherical Law of Cosines to find the distance
// between two lat/long points
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
	return distance;}

function degreesToRadians(degrees) {
	radians = (degrees * Math.PI)/180;
	return radians;}

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


