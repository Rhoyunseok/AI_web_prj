window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 36.62559389150519, lng: 127.45439887046814 },
        zoom: 13.5,
    });


    const malls = [
        { label: "TR", name: "백만장자의 막걸리", lat: 36.6330071124582, lng: 127.457739133089 },
        { label: "TR", name: "술먹고고래고래", lat: 36.6330071124582, lng: 127.457739133089 },
        { label: "TR", name: "청학동얼음막걸리", lat: 36.6344510092308, lng: 127.449761249993 },
        { label: "TR", name: "청송얼음막걸리", lat: 36.6326472307187, lng: 127.458551639034 },
        { label: "TR", name: "달빛양조장", lat: 36.632352991992, lng: 127.458463132785 },
        { label: "TR", name: "청송얼음막걸리가경점", lat: 36.6302970721725, lng: 127.435990924128 },
        { label: "TR", name: "전주한상막걸리", lat: 36.6355145572487, lng: 127.432546641702 },
        { label: "TR", name: "사케라쿠", lat: 36.611938754906, lng: 127.46950443769 },
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