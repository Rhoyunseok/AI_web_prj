window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 36.62813149999999, lng: 127.4563596 },
        zoom: 18,
    });


    const malls = [
        { label: "D", name: "RnD", lat: 36.6328032376479, lng: 127.458382167373 },
        { label: "D", name: "D&D (디앤디)", lat: 36.631131900581, lng: 127.460698056873 },
        { label: "D", name: "이올렛", lat: 36.6339933028659, lng: 127.459986759708 },
        { label: "D", name: "사막의 하얀꽃", lat: 36.632947811583, lng: 127.458958838156 },
        { label: "D", name: "KUSH", lat: 36.6331936301859, lng: 127.458937934206 },
        { label: "D", name: "190바 Bar", lat: 36.6394316, lng: 127.4329238 },
        { label: "D", name: "아지트바", lat: 36.6394316, lng: 127.4329238 },
        { label: "D", name: "청주 더몰트", lat:36.6401462612783 , lng: 127.427683465632},
        { label: "D", name: "쥬키프", lat: 36.6647608582867, lng: 127.497899885187},
        { label: "D", name: "아이스앤보틀", lat: 36.6410298086309, lng: 127.422611030093}
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
            infowindow.setContent(name);//마커 클릭하면 상세정보 name 뜬다
            infowindow.open({
                anchor: marker,
                map,
            });
        });
    });

};