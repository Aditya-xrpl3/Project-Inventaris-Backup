import React, {useEffect, useState} from 'react';
import { Html5QrcodeScanner } from 'html5-qrcode';
import { useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function ScanPage() {
  const [scanResult, setScanResult] = useState(null);
  const [lokasiData, setLokasiData] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const scanner = new Html5QrcodeScanner('reader', {
      qrbox: {
        width: 250,
        height: 250,
      },
      fps: 5,
    }, false);

    function onScanSuccess(qrCodeMessage) {
      scanner.clear();
      setScanResult(qrCodeMessage);
    }

    function onScanFailure() {

    }

    scanner.render(onScanSuccess, onScanFailure);

    return () => {
      scanner.clear();
    };
  }, []);

  useEffect(() => {
    if (scanResult) {
      api.get(`/lokasi/${scanResult}/`)
        .then(response => {
          setLokasiData(response.data);
        })
        .catch(err => {
          setError('Gagal mengambil data lokasi.')
          console.error(err)
        });
    }
  }, [scanResult]);

  const handleLaporClick = (barangId) => {
    navigate(`/lapor/${barangId}`);
  };

  return (
    <div>
      <h2>Scan QR Code di Meja</h2>
      {!lokasiData && <div id="reader" style={{ width: '300px' }}></div>}

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {lokasiData && (
        <div>
          <h3>Lokasi: {lokasiData.nama_lokasi}</h3>
          <p>{lokasiData.deskripsi}</p>
          <h4>Daftar Barang:</h4>
          <ul>
            {lokasiData.barang_set.map(barang => (
              <li key={barang.id}>
                {barang.nama_barang} ({barang.status})
                {/* Button Lapor */}
                <button
                  onClick={() => handleLaporClick(barang.id)}
                  style={{ marginLeft: '10px' }}
                >
                  Lapor Kerusakan
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}