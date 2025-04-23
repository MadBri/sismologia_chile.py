from obspy import read

     def procesar_sismo(archivo: str, freq_min: float, freq_max: float):
         st = read(archivo)
         st_filtrado = st.copy()
         st_filtrado.filter("bandpass", freqmin=freq_min, freqmax=freq_max)
         st_filtrado.write(f"datos/procesados/filtrado_{freq_min}_{freq_max}Hz.mseed", format="MSEED")
         return st_filtrado
