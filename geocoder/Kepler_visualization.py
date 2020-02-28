from keplergl import KeplerGl 


# df needs to contain 'latitude' and 'longitude' columns
map_ = KeplerGl(height=700)
map_.add_data(df, 'Data')
map_.save_to_html(file_name='try.html')

