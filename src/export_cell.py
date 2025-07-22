def export_cell(cell, idx):
    geometry = cell.geometry()
    image = dem.clip(geometry)

    task = ee.batch.Export.image.toDrive(
        image=image,
        description=f'DEMtile{idx}',
        folder='DEM_Huila',
        fileNamePrefix=f'DEMtile{idx}',
        region=geometry,
        scale=30,
        maxPixels=1e13
    )
    task.start()
    print(f"Exportando DEMtile{idx}...")



def export_cell_Clim(cell, idx):
    geometry = cell.geometry()
    image = raster_clim.clip(geometry)

    task = ee.batch.Export.image.toDrive(
        image=image,
        description=f'Climtile{idx}',
        folder='Clim_Huila',
        fileNamePrefix=f'Climtile{idx}',
        region=geometry,
        scale=30,
        maxPixels=1e13
    )
    task.start()
    print(f"Exportando Climtile{idx}...")

