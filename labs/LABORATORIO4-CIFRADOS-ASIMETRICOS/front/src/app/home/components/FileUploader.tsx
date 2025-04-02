 
'use client';

import { useState } from 'react';
import { uploadFile } from '@/services/api';

export default function FileUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [privateKey, setPrivateKey] = useState<CryptoKey | null>(null);
  const [status, setStatus] = useState('');

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0] || null;
    setFile(selected);
  };

  const handlePrivateKeyImport = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const content = await file.text();

    const binary = atob(content
      .replace(/-----.*-----/g, '')
      .replace(/\s/g, '')
    );

    const binaryArray = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      binaryArray[i] = binary.charCodeAt(i);
    }

    try {
      const key = await crypto.subtle.importKey(
        'pkcs8',
        binaryArray.buffer,
        {
          name: 'RSASSA-PKCS1-v1_5',
          hash: 'SHA-256',
        },
        false,
        ['sign']
      );
      setPrivateKey(key);
      setStatus('Clave privada cargada correctamente.');
    } catch {
      setStatus('Error al importar la clave privada.');
    }
  };

  const handleUpload = async () => {
    if (!file || !privateKey) {
      setStatus('Por favor selecciona un archivo y carga tu clave privada.');
      return;
    }

    const buffer = await file.arrayBuffer();

    // 🔐 Hashear archivo
    const hashBuffer = await crypto.subtle.digest('SHA-256', buffer);
    const hash = btoa(String.fromCharCode(...new Uint8Array(hashBuffer)));

    // 📝 Firmar hash
    const signatureBuffer = await crypto.subtle.sign(
      { name: 'RSASSA-PKCS1-v1_5' },
      privateKey,
      hashBuffer
    );
    const signature = btoa(String.fromCharCode(...new Uint8Array(signatureBuffer)));

    // 📤 Subir archivo
    try {
      const res = await uploadFile(file, signature);
      setStatus('Archivo subido exitosamente.');
      console.log(res);
    } catch (err) {
      console.error(err);
      setStatus('Error al subir archivo.');
    }
  };

  return (
    <div className="flex flex-col items-start space-y-4">
      <h2 className="text-xl font-semibold">Subir archivo firmado</h2>

      <input type="file" onChange={handleFileChange} />

      <label className="text-sm text-gray-600">
        Cargar clave privada (.pem)
      </label>
      <input type="file" accept=".pem" onChange={handlePrivateKeyImport} />

      <button
        onClick={handleUpload}
        className="bg-green-600 text-white px-4 py-2 rounded"
      >
        Firmar y subir archivo
      </button>

      <p className="text-sm text-blue-600">{status}</p>
    </div>
  );
}
