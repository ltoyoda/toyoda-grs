//File part of geo_input.HTML
// Use this file to calculate distances from the study area using forms

    <script>
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
          ga('create', 'UA-1008641-85', 'auto');
          ga('send', 'pageview');
    </script>

    <script type="application/ld+json">{"@context":"http://schema.org","@type":"WebSite","name":"Lat Long","alternateName":"Latitude and Longitude",
    				"url":"http://www.latlong.net/","sameAs":["https://plus.google.com/+LatlongNet"]}</script>
        <script>
        var head=document.getElementsByTagName("head")[0],insertBefore=head.insertBefore;head.insertBefore=function(e,o){
        	e.href&&0===e.href.indexOf("https://fonts.googleapis.com/css?family=Roboto")||insertBefore.call(head,e,o)};
        var yid ='lat-long-address';
        function gotop(){
        	return document.body.scrollTop=document.documentElement.scrollTop=0,!1
        	}
        	window.onscroll=function(){
        	var o=document.getElementsByTagName("body")[0].scrollTop;
        	o>=100?document.getElementById("cd-top").className="cd-top cd-is-visible":document.getElementById("cd-top").className="cd-top"
        	};

        function pscm(e){
        	e.preventDefault&&e.preventDefault();
        	var t=document.getElementById("commentname").value,n=document.getElementById("commenttext").value,m=new XMLHttpRequest,
        	a="commentname="+encodeURIComponent(t)+"&yid="+encodeURIComponent(yid)+"&commenttext="+encodeURIComponent(n);
        	return m.open("POST","/_addcomment.php",!0),m.setRequestHeader("Content-type","application/x-www-form-urlencoded"),
        	m.onreadystatechange=function(){4===m.readyState&&200===m.status?(document.getElementById("tagmessage").innerHTML="Your comment saved successfully and will publish after approval.",
        	document.getElementById("commentname").value="",document.getElementById("commenttext").value=""):document.getElementById("tagmessage").innerHTML="There was an error, please try again later.",
        	document.getElementById("tagmessage").style.visibility="visible"},m.send(a),!1}
        	var frmcomment=document.getElementById("frmcomment");frmcomment.attachEvent?frmcomment.attachEvent("submit",pscm):frmcomment.addEventListener("submit",pscm);
        </script>

    <script>!function(e,t){function n(){t.getElementById("navmenu").classList.toggle("list-vertical"),t.getElementsByTagName("header")[0].classList.toggle("open"),
t.getElementsByTagName("body")[0].classList.toggle("open")}function s(){o.classList.contains("open")?setTimeout(n,500):n(),o.classList.toggle("open"),
t.getElementsByTagName("main")[0].classList.toggle("open")}function i(){o.classList.contains("open")&&s()}var o=t.getElementById("menu"),a="onorientationchange"in e?"orientationchange":"resize";
t.getElementById("toggle").addEventListener("click",function(){s()}),e.addEventListener(a,i)}(this,this.document);</script>


//        <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><script type="text/javascript">
//        function initialize(){var e = new google.maps.LatLng(1.1, 1.1), o = {zoom:5, center:e, panControl:!0, scaleControl:!0, scrollwheel:!1, overviewMapControl:!0, overviewMapControlOptions:{opened:!0}, mapTypeId:google.maps.MapTypeId.HYBRID}; map = new google.maps.Map(document.getElementById("latlongmap"), o), marker = new google.maps.Marker({position:e, map:map}), geocoder = new google.maps.Geocoder, map.streetViewControl = !1, infowindow = new google.maps.InfoWindow({content:"(1.10, 1.10)"}), google.maps.event.addListener(map, "click", function(e){marker.setPosition(e.latLng); var o = e.latLng, n = "(" + o.lat().toFixed(6) + " , " + + o.lng().toFixed(6) + ")"; infowindow.setContent(n), google.maps.event.addListener(marker, "click", function(){infowindow.open(map, marker)}), infowindow && infowindow.close(), infowindow.open(map, marker), document.getElementById("lat").value = o.lat().toFixed(6), document.getElementById("lng").value = o.lng().toFixed(6), document.getElementById("latlngspan").innerHTML = n, document.getElementById("coordinatesurl").value = "http://www.latlong.net/c/?lat=" + o.lat().toFixed(6) + "&long=" + o.lng().toFixed(6), dec2dms()}), google.maps.event.addListener(map, "mousemove", function(e){var o = e.latLng; document.getElementById("mlat").innerHTML = "(" + o.lat().toFixed(6) + ", " + o.lng().toFixed(6) + ")"})}function showlatlong(e){e.preventDefault && e.preventDefault(); var o = new google.maps.LatLng(document.getElementById("lat").value, document.getElementById("lng").value); map.setCenter(o), marker.setPosition(o), map.setZoom(12); var n = "(" + o.lat().toFixed(6) + " , " + + o.lng().toFixed(6) + ")"; document.getElementById("latlngspan").innerHTML = n, document.getElementById("coordinatesurl").value = "http://www.latlong.net/c/?lat=" + o.lat().toFixed(6) + "&long=" + o.lng().toFixed(6), infowindow.setContent(n), infowindow && infowindow.close(), google.maps.event.addListener(marker, "click", function(){infowindow.open(map, marker)}), dec2dms(), codeLatLng(o)}function codeLatLng(e){geocoder.geocode({latLng:e}, function(o, n){n === google.maps.GeocoderStatus.OK?o[1]?(marker.setPosition(e), infowindow.setContent(o[1].formatted_address), infowindow.open(map, marker), document.getElementById("address").value = o[1].formatted_address):alert("No results found"):alert("Geocoder failed due to: " + n)})}var latlongform = document.getElementById("latlongform"); latlongform.attachEvent?latlongform.attachEvent("submit", showlatlong):latlongform.addEventListener("submit", showlatlong); var map, marker, infowindow, geocoder;
//        function dec2dms(){var e = document.getElementById("lat").value, t = document.getElementById("lng").value; document.getElementById("dms-lat").innerHTML = getdms(e, !0), document.getElementById("dms-lng").innerHTML = getdms(t, !1)}function getdms(e, t){var n = 0, m = 0, l = 0, a = "X"; return a = t && 0 > e?"S":!t && 0 > e?"W":t?"N":"E", d = Math.abs(e), n = Math.floor(d), l = 3600 * (d - n), m = Math.floor(l / 60), l = Math.round(1e4 * (l - 60 * m)) / 1e4, n + "&deg; " + m + "' " + l + "'' " + a}
//        </script>

//        </script>
//    <script src="https://maps.googleapis.com/maps/api/js?callback=initialize&amp;key=AIzaSyCt2JrdlwkZXbfc9lrdAtCGm6ki32boS6s" async defer></script>
//

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
