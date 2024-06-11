window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 36.62559389150519, lng: 127.45439887046814 },
        zoom: 14,
    });


    const malls = [
        { label: "C", name: "RnD", lat: 36.6328032376479, lng: 127.458382167373 },
        { label: "C", name: "D&D (디앤디)", lat: 36.631131900581, lng: 127.460698056873 },
        { label: "C", name: "이올렛", lat: 36.6339933028659, lng: 127.459986759708 },
        { label: "C", name: "사막의 하얀꽃", lat: 36.632947811583, lng: 127.458958838156 },
        { label: "C", name: "KUSH", lat: 36.6331936301859, lng: 127.458937934206 },
        { label: "C", name: "190바 Bar", lat: 36.6394316, lng: 127.4329238 },
        { label: "C", name: "아지트바", lat: 36.6394316, lng: 127.4329238 },

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