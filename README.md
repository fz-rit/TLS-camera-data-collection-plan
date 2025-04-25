# TLS-camera-data-collection-plan

## **What**  
Collection of terrestrial LiDAR point clouds and co-registered RGB images of forested areas using a ground-based LiDAR scanner and either a DSLR camera or a smartphone. The data will be used for:  
- Tree part segmentation (e.g., stem, branches, leaves)  
- Single tree segmentation (individual tree identification)  
- 3D reconstruction and structural analysis of trees  

## **Why**  
The goal is to generate a high-quality, multimodal dataset for developing and evaluating deep learning and geometric algorithms in forest structure analysis. Applications include:  
- Forest inventory and ecological monitoring  
- Biomass estimation  
- Enhanced semantic understanding of complex vegetation  
- Ground truth creation for algorithm benchmarking  

## **When**  
*Planned Schedule:*  
- [ ] Week of ___ (e.g., May 6–10, 2025): Site preparation and equipment testing  
- [ ] Week of ___: Data collection sessions (2–3 days depending on weather)  
- [ ] Week of ___: Backup dates in case of delays (e.g., due to rain or technical issues)  

## **Where**  
*Primary Site:*  
- [Insert location, e.g., "RIT campus forest patch behind Gannett Building"]  
- [Optional] Secondary backup site: [another known accessible forest patch]  

## **Who**  
- **PI:** Fei Zhang (Postdoc Researcher)  
- **Support Team:**  
  - [Name], LiDAR operator  
  - [Name], camera operator / image annotator  
  - [Name], logistics & field safety support  

## **How**  
**Equipment:**  
- LiDAR: [e.g., RIEGL VZ-400i / Velodyne Alpha Puck / FARO Focus 3D]  
- Camera: [e.g., iPhone 13 Pro / Nikon D850] with GPS tagging  
- Tripod, angle calibration tools, scale references (e.g., checkerboard or meter sticks)  

**Workflow:**  
1. **Site preparation:** Clear line-of-sight for LiDAR, mark ground truth reference points  
2. **LiDAR scanning:** Multiple stations per plot to capture 360° coverage, with overlap  
3. **Image capture:** RGB images from multiple angles with varying elevation and azimuth  
4. **Metadata logging:** Time, GPS, weather, and scanner setup notes  
5. **Data registration:** Align LiDAR scans and RGB images via GPS/GNSS or manual ICP  
6. **Post-processing:** Noise filtering, semantic labeling, segmentation model training  

---

Let me know if you'd like help filling in equipment specs, location details, or refining the schedule based on your project timeline.