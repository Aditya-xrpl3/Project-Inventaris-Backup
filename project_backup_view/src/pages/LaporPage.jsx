import React, { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';

export default function LaporPage() {
  const { barangId } = useParams();
  const navigate = useNavigate();
  
  const [nama, setNama] = useState('');
  const [kelas, setKelas] = useState('');
  const [nisn, setNisn] = useState('');
  const [deskripsi, setDeskripsi] = useState('');
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    setError(null);

    const dataLaporan = {
      barang: barangId,
      deskripsi: deskripsi,
      nama_pelapor: nama,
      kelas: kelas,
      nisn: nisn,
    };

    try {
      await api.post('/lapor/', dataLaporan);
      setMessage('Laporan berhasil dikirim! Terima kasih.');

      setTimeout(() => {
        navigate('/scan');
      }, 2000);
    } catch (err) {
      setError('Gagal mengirim laporan. Silakan coba lagi.');
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Form Laporan Kerusakan</h2>
      <p>Anda melaporakan kerusakan untuk barang dengan ID: {barangId}</p>

      <form onSubmit={handleSubmit}>
        <div>
          <label>Nama Pelapor:</label>
          <input
          type="text"
          value={nama}
          onChange={(e) => setNama(e.target.value)}
          required
          />
        </div>
        <div>
          <label>Kelas:</label>
          <input
          type='text'
          value={kelas}
          onChange={(e) => setKelas(e.target.value)}
          required
          />
        </div>
        <div>
          <label>Nisn (Opsional):</label>
          <input
          type="text"
          value={nisn}
          onChange={(e) => setNisn(e.target.value)}
         />
        </div>
        <div>
          <label>Deskripsi Kerusakan:</label>
          <textarea
          value={deskripsi}
          onChange={(e) => setDeskripsi(e.target.value)}
          rows="4"
          required
          />
        </div>
        {/* Tidak boleh submit 2x */}
        <button type='submit' disabled={!!message}>
          Kirim Laporan
        </button>
      </form>

      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}