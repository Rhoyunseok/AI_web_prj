window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 36.62813149999999, lng: 127.4563596 },
        zoom: 18,
    });


    const malls = [
        { label: "W", name: "세계주류전문점", lat: 36.6465957230681, lng: 127.477808510126 },
        { label: "W", name: "와인", lat: 36.6337496701244, lng: 127.490147771227 },
        { label: "W", name: "와인가게 23에 따쥐", lat: 36.6125563104797, lng: 127.465943432802 },
        { label: "W", name: "화제집중", lat: 36.6478038440069, lng: 127.47718402173 },
        { label: "W", name: "와인바산남점", lat: 36.6119944506692, lng: 127.4664741294 },
        { label: "W", name: "와인곳간", lat: 36.6119944506692, lng: 127.46647412943 },
    ];

    const bounds = new google.maps.LatLngBounds();
    const infowindow = new google.maps.InfoWindow();


    malls.forEach(({ label, name, lat, lng }) => {
        const marker = new google.maps.Marker({
            position: { lat, lng },
            label,
            map,
        });
        bounds.extend(marker.position);

        marker.addListener("click", () => {
            map.panTo(marker.position);// 지도 중심으로 이동
            infowindow.setContent(name);
            infowindow.open({
                anchor: marker,
                map,
            });
        });
    });

};