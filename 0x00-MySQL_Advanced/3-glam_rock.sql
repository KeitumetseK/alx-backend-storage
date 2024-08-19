-- Task 3: List all bands with Glam rock as their main style, ranked by longevity
SELECT band_name, 
       IFNULL(YEAR(2022) - formed, 0) - IFNULL(YEAR(2022) - split, 0) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;

