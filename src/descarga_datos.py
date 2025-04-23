from obspy.clients.fdsn import Client
     from obspy import UTCDateTime

     def descargar_datos():
         client = Client("IRIS")
         st = client.get_waveforms(
             network="IU",
             station="CMLA",
             location="",
             channel="BHZ",
             starttime=UTCDateTime("2025-01-02T20:43:00"),
             endtime=UTCDateTime("2025-01-02T20:48:00")
         )
         st.write("datos/crudos/terremoto_chile.sac", format="SAC")

     if __name__ == "__main__":
         descargar_datos() 
