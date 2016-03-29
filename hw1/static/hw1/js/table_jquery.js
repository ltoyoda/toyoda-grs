//File part of geo.HTML
// Use this file to calculate distances from the study area using forms
// modified from myLoc.js

$(document).ready(function( ) {
	$('table.striped tr:even').addClass('even');
});







//
////File part of geo.HTML
///* myLoc.js */
//var map = null;
//var ourCoords =  {      // for calculating the diatance
//	latitude: 52.0818522,
//	longitude: 4.2902251
//};
//
////window.onload = getMyLocation;  //run it when the page is loaded
//
//function getMyLocation() {
//	if (navigator.geolocation) {    //checks if there is geolocation in the browser
//
//		navigator.geolocation.getCurrentPosition(   //runs the 2 functions below and error
//			displayLocation,
//			displayError);
//	}
//	else {
//		alert("Oops, no geolocation support");
//	}
//}
//
//function displayLocation(position) {    //gets the attributes lat and long and displays it
//	var latitude = position.coords.latitude;
//	var longitude = position.coords.longitude;
//// For the actual position
//	var div = document.getElementById("location");
//// Displays local position
//	div.innerHTML = "You are at Latitude: " + latitude + ", Longitude: " + longitude;
//// For the distance from the coordinates set in line 4
//	var km = computeDistance(position.coords, ourCoords);  //using the code below
//	var distance = document.getElementById("distance");
//// and displays the distance
//	distance.innerHTML = "You are " + km + " km from the TOYODA's Headquarters!";
//// for loading the map
//	showMap(position.coords);
//}
//// -----------------------------------------------------------
//// Uses the Spherical Law of Cosines to find the distance
//// between two lat/long points
//function computeDistance(startCoords, destCoords) {
//	var startLatRads = degreesToRadians(startCoords.latitude);
//	var startLongRads = degreesToRadians(startCoords.longitude);
//	var destLatRads = degreesToRadians(destCoords.latitude);
//	var destLongRads = degreesToRadians(destCoords.longitude);
//
//	var Radius = 6371; // radius of the Earth in km
//	var distance = Math.acos(Math.sin(startLatRads) * Math.sin(destLatRads) +
//					Math.cos(startLatRads) * Math.cos(destLatRads) *
//					Math.cos(startLongRads - destLongRads)) * Radius;
//	return distance;
//}
//
//function degreesToRadians(degrees) {
//	radians = (degrees * Math.PI)/180;
//	return radians;
//}
//// ------------------------------------------------------
//// For showing the map on the page
//function showMap(coords) {
//	var googleLatAndLong = new google.maps.LatLng(coords.latitude,
//												  coords.longitude);
//	var mapOptions = {
//		zoom: 7, //small number = zoom in
//		center: googleLatAndLong,
//		mapTypeId: google.maps.MapTypeId.HYBRID  // use also ROADMAP, SATELLITE, TERRAIN
//	};
//	var mapDiv = document.getElementById("map");// from the html class id
//	map = new google.maps.Map(mapDiv, mapOptions);
//
//	// add the user marker
//	var title = "Your Location";
//    var content = "You are here: " + coords.latitude + ", " + coords.longitude;
//    addMarker(map, googleLatAndLong, title, content);
//}
//
////-----------------------------------------------------------------------
//// For the pin - Marker
//function addMarker(map, latlong, title, content) {
//	var markerOptions = {
//		position: latlong,
//		map: map,
//		title: title,
//		clickable: true
//	};
//	var marker = new google.maps.Marker(markerOptions);
//
//	var infoWindowOptions = {
//		content: content,
//		position: latlong
//	};
//
//	var infoWindow = new google.maps.InfoWindow(infoWindowOptions);
//
//	google.maps.event.addListener(marker, 'click', function() {
//		infoWindow.open(map);
//	});
//}
////-------------------------------------------------------------------------------
//// Error display
//function displayError(error) {
//	var errorTypes = {
//		0: "Unknown error",
//		1: "Permission denied",
//		2: "Position is not available",
//		3: "Request timeout"
//	};
//	var errorMessage = errorTypes[error.code];
//	if (error.code == 0 || error.code == 2) {
//		errorMessage = errorMessage + " " + error.message;
//	}
//	var div = document.getElementById("location");
//	div.innerHTML = errorMessage;
//}
//
