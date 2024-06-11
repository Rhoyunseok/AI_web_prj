window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 36.62559389150519, lng: 127.45439887046814 },
        zoom: 13.5,

    });


    const malls = [
        { label: "B", name: "무지개맥주충북대정문점", lat: 36.6352554, lng: 127.4386333 },
        { label: "B", name: "역전할머니맥주 충북대점", lat: 36.6327273026081, lng:  127.458046292656},
        { label: "B", name: "홀리데이펍", lat: 36.6321727131295, lng: 127.457374960333 },
        { label: "B", name: "맥주창고", lat: 36.6327372706902 , lng: 127.458031816571 },
        { label: "B", name: "가장맛있는맥주집", lat: 36.6225235221169, lng: 127.446703145266 },
        { label: "B", name: "폼프리츠",lat: 36.6321743279182, lng: 127.457963301046 },
        { label: "B", name: "크라운호츠 충북대", lat: 36.6331743499364, lng: 127.459264302026 },
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