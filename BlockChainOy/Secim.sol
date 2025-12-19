// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecimSistemi {
    struct Aday { uint id; string isim; uint oySayisi; }
    
    mapping(uint => Aday) public adaylar;
    
    // ARTIK CÜZDANI DEĞİL, TC NO'YU TAKİP EDİYORUZ
    mapping(string => bool) public oyKullandiMi; 
    
    uint public adaySayisi;

    function adayEkle(string memory _isim) public {
        adaySayisi++;
        adaylar[adaySayisi] = Aday(adaySayisi, _isim, 0);
    }

    // Fonksiyon artık TC NO da istiyor
    function oyVer(string memory _tcNo, uint _adayId) public {
        require(!oyKullandiMi[_tcNo], "Bu TC Kimlik No ile zaten oy kullanildi!");
        
        oyKullandiMi[_tcNo] = true; // TC'yi işaretle
        adaylar[_adayId].oySayisi++; // Oyu artır
    }
}