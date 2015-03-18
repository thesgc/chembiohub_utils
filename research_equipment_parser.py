#!/usr/bin/python
          # -*- coding: utf8 -*-
from bs4 import BeautifulSoup


page = """

<!DOCTYPE html>
<!--[if lt IE 7 ]> <html lang="en" class="ie ie6"> <![endif]-->
<!--[if IE 7 ]>    <html lang="en" class="ie ie7"> <![endif]-->
<!--[if IE 8 ]>    <html lang="en" class="ie ie8"> <![endif]-->
<!--[if IE 9 ]>    <html lang="en" class="ie ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!-->
<html lang="en">
<!--<![endif]-->
<head>
  <meta charset="utf-8">
  <!--[if lt IE 9]>
  <script src="//static.data.ox.ac.uk/lin/html5shiv.min.js"></script>
  <![endif]-->

  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/lib/jquery-ui/css/smoothness/jquery-ui-1.8.custom.css"></script>

  <!-- print stylesheet for print stlying -->
  <link media="print" href="//static.data.ox.ac.uk/equipment/css/print.css" rel="stylesheet" type="text/css" />

  <!-- general reset styles for getting rid of annoying browser defaults -->
  <link media="all" href="//static.data.ox.ac.uk/equipment/css/reset.css" rel="stylesheet" type="text/css" />

  <!-- basic styles suitable for all devices *DO not put layout stuff here * -->
  <link media="all" href="//static.data.ox.ac.uk/equipment/css/basic.css" rel="stylesheet" type="text/css" />

  <!-- styles for mobile devices-->
  <link href="//static.data.ox.ac.uk/equipment/css/tiny.css" rel="stylesheet" type="text/css" media="screen and (max-width: 639px)" />

  <!-- styles for smallscreen devices-->
  <link href="//static.data.ox.ac.uk/equipment/css/small.css" rel="stylesheet" type="text/css" media="(min-width: 640px)" />

  <!-- styles for small-to-medium screen desktop  devices-->
  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/equipment/css/medium.css" media="(min-width: 999px) and (max-width: 1600px)" />

  <!-- styles for large screen desktop devices-->
  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/equipment/css/large.css" media="screen and (min-width: 1601px)" />

  <!-- pull in tiny responsive sheets for mobile IE  -->
  <!--[if (lt IE 9)&(!IEMobile)]>
  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/equipment/css/tiny.css" media="screen"/>
  <![endif]-->


  <!-- pull in small and medium responsive sheets for desktop IE that doesn't understand media queries (i.e. before IE 9) -->
  <!--[if (lt IE 9)&(!IEMobile)]>
  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/equipment/css/small.css" media="screen"/>
  <link rel="stylesheet" type="text/css" href="//static.data.ox.ac.uk/equipment/css/medium.css" media="screen"/>
  <![endif]-->

  <!-- styles for Internet explorer  ie-specific styles -->
  <!--[if (gt IE 4)&(lt IE 9)]>
  <link media="screen" href="//static.data.ox.ac.uk/equipment/css/ie.css" rel="stylesheet" type="text/css"/>
  <![endif]-->



<link rel="stylesheet" media="screen" href="//active.oucs.ox.ac.uk/shared/stylesheet/analytics/analytics.css" type="text/css"/>


  <meta name="keywords" content="" />
  <meta name="description" content="" />
  <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1"/>
  <link rel="shortcut icon" type="image/x-icon" href="//static.data.ox.ac.uk/favicon.ico" />
  
  <script type="text/javascript">
    var staticURL = "//static.data.ox.ac.uk/";
    var searchURL = "/search/";
  </script>
  <script type="text/javascript" src="//static.data.ox.ac.uk/lib/jquery/jquery.min.js"></script>
  <script   type="text/javascript" src="//static.data.ox.ac.uk/lib/jquery.collapsible.min.js" charset="utf-8"></script>
  <script type="text/javascript" src="//static.data.ox.ac.uk/lib/jquery-ui/jquery-ui.min.js"></script>
  <script type="text/javascript" src="//static.data.ox.ac.uk/lib/openlayers/OpenLayers.js"></script>
  <script   type="text/javascript" src="//static.data.ox.ac.uk/app/dataox-1.0.min.js" charset="utf-8"></script>
  <script   type="text/javascript" src="//static.data.ox.ac.uk/equipment.min.js" charset="utf-8"></script>
  
  

  <title>Browse | Research Facilities and Equipment at Oxford</title>
</head>

<body data-dataox-search-url="/search/" class="equipment-browse equipment-browse-index">
  <div id="page">
    <header class="pageHeader">
      <div class="siteTitle"><a href="/" id="homeLink">Research Facilities and Equipment at Oxford</a></div>

      <a href="http://www.ox.ac.uk/" id="oxCrest">University of Oxford</a>
    </header>
    <div class="main">

      <article class="content">
      <div class="wrapper with-left-sidebar">
          
      
  



<h1>Categories (Oxford equipment only)</h1>



<p>All pieces of equipment have been categorised according to the experimental
   technique that they are mainly associated with. Similar techniques or those
   associated with a particular field of study have been grouped together,
   enabling a two-tier searchable system. Any suggestions for
   re-categorisation should be made via the <a href="/contact/">contact page</a>.</p>



<h2 class="hidden">Sub-categories</h2>
<ul class="equipment-categories">

  <li class="equipment-category">
    <h3><a href="/browse/biomolecular-interaction-analysis/">Biomolecular Interaction Analysis</a></h3>
    
    <ul>
      <li><a href="/browse/biomolecular-interaction-analysis/bio-layer-interferometry/">Bio-Layer Interferometry (BLI)</a></li>
      <li><a href="/browse/biomolecular-interaction-analysis/surface-plasmon-resonance/">Surface Plasmon Resonance (SPR)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/cardiovascular-physiology/">Cardiovascular Physiology</a></h3>
    
    <ul>
      <li><a href="/browse/cardiovascular-physiology/applanation-tonometry/">Applanation Tonometry</a></li>
      <li><a href="/browse/cardiovascular-physiology/cardiac-mapping/">Cardiac Mapping</a></li>
      <li><a href="/browse/cardiovascular-physiology/electrocardiography/">Electrocardiography (ECG)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/cell-nucleic-acid-protein-analysis/">Cell / Nucleic Acid / Protein Analysis</a></h3>
    
    <ul>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/cell-counting/">Cell Counting</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/cell-nucleic-acid-and-protein-analysis/">Cell, Nucleic Acid and Protein Analysis</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/haematology-analysis/">Haematology Analysis</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/nucleic-acid-analysis/">Nucleic Acid Analysis</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/nucleic-acid-and-protein-analysis/">Nucleic Acid and Protein Analysis</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/protein-analysis/">Protein Analysis</a></li>
      <li><a href="/browse/cell-nucleic-acid-protein-analysis/real-time-cell-analysis/">Real-Time Cell Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/cell-preparation/">Cell Preparation</a></h3>
    
    <ul>
      <li><a href="/browse/cell-preparation/cell-disruption/">Cell Disruption</a></li>
      <li><a href="/browse/cell-preparation/cell-expansion/">Cell Expansion</a></li>
      <li><a href="/browse/cell-preparation/cell-isolation/">Cell Isolation</a></li>
      <li><a href="/browse/cell-preparation/cell-processing/">Cell Processing</a></li>
      <li><a href="/browse/cell-preparation/cell-sorter/">Cell Sorter </a></li>
      <li><a href="/browse/cell-preparation/fermentor/">Fermentor</a></li>
      <li><a href="/browse/cell-preparation/micromanipulation/">Micromanipulation</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/cell-based-assays/">Cell-based assays</a></h3>
    
    <ul>
      <li><a href="/browse/cell-based-assays/studying-cells-under-flow-shear-stress/">Studying cells under flow/shear stress</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/centrifugation/">Centrifugation</a></h3>
    
    <ul>
      <li><a href="/browse/centrifugation/analysis/">Analysis</a></li>
      <li><a href="/browse/centrifugation/analytical-ultracentrifugation/">Analytical Ultracentrifugation</a></li>
      <li><a href="/browse/centrifugation/high-performance-centrifugation/">High Performance Centrifugation</a></li>
      <li><a href="/browse/centrifugation/micro-ultracentrifugation/">Micro-Ultracentrifugation</a></li>
      <li><a href="/browse/centrifugation/preparative-ultracentrifugation/">Preparative Ultracentrifugation</a></li>
      <li><a href="/browse/centrifugation/sample-prep/">Sample Prep</a></li>
      <li><a href="/browse/centrifugation/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/chromatography/">Chromatography</a></h3>
    
    <ul>
      <li><a href="/browse/chromatography/denaturing-high-performance-liquid-chromatography/">Denaturing High Performance Liquid Chromatography (DHPLC)</a></li>
      <li><a href="/browse/chromatography/fplc/">FPLC</a></li>
      <li><a href="/browse/chromatography/fast-protein-liquid-chromatography/">Fast Protein Liquid Chromatography (FPLC)</a></li>
      <li><a href="/browse/chromatography/field-flow-fractionation/">Field Flow Fractionation (FFF)</a></li>
      <li><a href="/browse/chromatography/gas-chromatography/">Gas Chromatography</a></li>
      <li><a href="/browse/chromatography/high-performance-liquid-chromatography/">High Performance Liquid Chromatography (HPLC)</a></li>
      <li><a href="/browse/chromatography/liquid-chromatography/">Liquid Chromatography</a></li>
      <li><a href="/browse/chromatography/size-exclusion-chromatograhy-multiple-angle-light-satter/">Size Exclusion Chromatograhy, Multiple Angle Light Satter</a></li>
      <li><a href="/browse/chromatography/ultra-high-performance-liquid-chromatography/">Ultra High Performance Liquid Chromatography (UHPLC)</a></li>
      <li><a href="/browse/chromatography/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/computing/">Computing</a></h3>
    
    <ul>
      <li><a href="/browse/computing/cloud-computing/">Cloud Computing</a></li>
      <li><a href="/browse/computing/co-location-service/">Co-Location Service</a></li>
      <li><a href="/browse/computing/high-throughput-computing/">High Throughput Computing</a></li>
      <li><a href="/browse/computing/supercomputing/">Supercomputing</a></li>
      <li><a href="/browse/computing/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/containment/">Containment</a></h3>
    
    <ul>
      <li><a href="/browse/containment/containment-hood/">Containment Hood</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/crystal-imaging/">Crystal Imaging</a></h3>
    
    <ul>
      <li><a href="/browse/crystal-imaging/stopped-flow/">Stopped Flow</a></li>
      <li><a href="/browse/crystal-imaging/plate-hotels-incubators/">plate hotels/incubators (with temp. control ).</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/crystallisation/">Crystallisation</a></h3>
    
    <ul>
      <li><a href="/browse/crystallisation/crystal-growth/">Crystal Growth</a></li>
      <li><a href="/browse/crystallisation/free-interface-diffusion/">Free Interface Diffusion (FID)</a></li>
      <li><a href="/browse/crystallisation/hanging-sitting-drop/">Hanging / Sitting Drop</a></li>
      <li><a href="/browse/crystallisation/high-throughput-protein-crystallisation/">High Throughput Protein Crystallisation</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/crystallography-x-ray-techniques/">Crystallography / X-Ray Techniques</a></h3>
    
    <ul>
      <li><a href="/browse/crystallography-x-ray-techniques/cryostream-cooler/">Cryostream Cooler</a></li>
      <li><a href="/browse/crystallography-x-ray-techniques/goniometer/">Goniometer</a></li>
      <li><a href="/browse/crystallography-x-ray-techniques/x-ray-reflectometry/">X-Ray Reflectometry (XRR)</a></li>
      <li><a href="/browse/crystallography-x-ray-techniques/x-ray-detection/">X-ray Detection</a></li>
      <li><a href="/browse/crystallography-x-ray-techniques/x-ray-diffraction/">X-ray Diffraction (XRD)</a></li>
      <li><a href="/browse/crystallography-x-ray-techniques/x-ray-generator/">X-ray Generator</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/densitometry/">Densitometry</a></h3>
    
    <ul>
      <li><a href="/browse/densitometry/bone-densitometry/">Bone Densitometry</a></li>
      <li><a href="/browse/densitometry/infant-body-composition/">Infant Body Composition</a></li>
      <li><a href="/browse/densitometry/total-body-composition/">Total Body Composition</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/electron-microscopy-sample-preparation/">Electron Microscopy Sample Preparation</a></h3>
    
    <ul>
      <li><a href="/browse/electron-microscopy-sample-preparation/critical-point-drying/">Critical Point Drying</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/cryopreparation/">Cryopreparation</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/freeze-substitution/">Freeze Substitution</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/ion-slicing/">Ion Slicing</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/sputter-coating/">Sputter Coating</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/transmission-electron-microscopy/">Transmission Electron Microscopy (TEM)</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/ultramicrotomy/">Ultramicrotomy</a></li>
      <li><a href="/browse/electron-microscopy-sample-preparation/vacuum-coating/">Vacuum Coating</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/electrophoresis/">Electrophoresis</a></h3>
    
    <ul>
      <li><a href="/browse/electrophoresis/2-dimensional-difference-gel-electrophoresis/">2-Dimensional Difference Gel Electrophoresis (2D-DIGE)</a></li>
      <li><a href="/browse/electrophoresis/continuous-flow-electrophoresis/">Continuous Flow Electrophoresis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/electrophysiology/">Electrophysiology</a></h3>
    
    <ul>
      <li><a href="/browse/electrophysiology/whole-cell-patch-clamp-sertup/">Whole-cell patch clamp sertup</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/flow-cytometry/">Flow Cytometry</a></h3>
    
    <ul>
      <li><a href="/browse/flow-cytometry/analysis/">Analysis</a></li>
      <li><a href="/browse/flow-cytometry/analysis-and-cell-sorting/">Analysis and Cell Sorting</a></li>
      <li><a href="/browse/flow-cytometry/cell-sorting/">Cell Sorting</a></li>
      <li><a href="/browse/flow-cytometry/flow-cytometer/">Flow Cytometer</a></li>
      <li><a href="/browse/flow-cytometry/quantitative-image-analysis/">Quantitative Image Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/flow-cytometry-mass-spectroscopy/">Flow Cytometry/mass spectroscopy</a></h3>
    
    <ul>
      <li><a href="/browse/flow-cytometry-mass-spectroscopy/analysis/">analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/fluorimetry/">Fluorimetry</a></h3>
    
    <ul>
      <li><a href="/browse/fluorimetry/differential-scanning-fluorimetry/">Differential Scanning Fluorimetry</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/gas-liquid-analysis/">Gas / Liquid Analysis</a></h3>
    
    <ul>
      <li><a href="/browse/gas-liquid-analysis/biochemical-analysis/">Biochemical Analysis</a></li>
      <li><a href="/browse/gas-liquid-analysis/blood-gas-analysis/">Blood Gas Analysis</a></li>
      <li><a href="/browse/gas-liquid-analysis/mercury-analysis/">Mercury Analysis</a></li>
      <li><a href="/browse/gas-liquid-analysis/nitric-oxide-analysis/">Nitric Oxide Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/gas-liquid-chromatography-mass-spectrometry/">Gas / Liquid Chromatography - Mass Spectrometry (GC-MS / LC-MS)</a></h3>
    
    <ul>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/gc-ms/">GC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/gas-chromatography-combustion-isotope-ratio-ms/">Gas Chromatography Combustion Isotope Ratio MS (GC-C-IRMS)</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/hplc/">HPLC</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/ion-trap-lc-ms/">Ion Trap LC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/ion-trap-lc-ms-ms/">Ion Trap LC-MS/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/lc-isotope-ratio-ms/">LC-Isotope Ratio MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/lc-ms/">LC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/maldi-qtof-lc-ms-ms/">MALDI-QTOF LC-MS/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/nano-lc-chip-qqq-ms/">Nano-LC CHIP QQQ-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/orbitrap-lc-ms-ms/">Orbitrap LC-MS/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/orbitrap-lc-ms/">Orbitrap LC/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/probe-ms/">Probe MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/q-tof-ms/">Q-TOF MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/qtof-gc-ms-ms/">QTOF GC-MS/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/qtof-lc-ms/">QTOF LC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/qtof-lc-ms-ms/">QTOF LC-MS/MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/quadrupole-gc-ms/">Quadrupole GC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/quadrupole-lc-ms/">Quadrupole LC-MS</a></li>
      <li><a href="/browse/gas-liquid-chromatography-mass-spectrometry/tof-lc-ms/">TOF LC-MS</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/genetic-techniques/">Genetic Techniques</a></h3>
    
    <ul>
      <li><a href="/browse/genetic-techniques/biomolecular-interactions/">Biomolecular Interactions</a></li>
      <li><a href="/browse/genetic-techniques/blood-analysis/">Blood analysis</a></li>
      <li><a href="/browse/genetic-techniques/cluster-generation/">Cluster Generation</a></li>
      <li><a href="/browse/genetic-techniques/dna-sequencing/">DNA Sequencing</a></li>
      <li><a href="/browse/genetic-techniques/gene-gun/">Gene Gun</a></li>
      <li><a href="/browse/genetic-techniques/genetic-analysis/">Genetic analysis</a></li>
      <li><a href="/browse/genetic-techniques/genetic-analysis-sequence-detection/">Genetic analysis/sequence detection</a></li>
      <li><a href="/browse/genetic-techniques/mutation-detection/">Mutation detection</a></li>
      <li><a href="/browse/genetic-techniques/nucleic-acid-extraction/">Nucleic Acid Extraction</a></li>
      <li><a href="/browse/genetic-techniques/nucleic-acid-purification/">Nucleic Acid Purification</a></li>
      <li><a href="/browse/genetic-techniques/nucleic-acid-workstation/">Nucleic Acid Workstation</a></li>
      <li><a href="/browse/genetic-techniques/pcr-setup/">PCR Setup</a></li>
      <li><a href="/browse/genetic-techniques/rt-pcr/">RT-pcr</a></li>
      <li><a href="/browse/genetic-techniques/real-time-pcr/">Real-time PCR</a></li>
      <li><a href="/browse/genetic-techniques/sequencing/">Sequencing</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/high-magnetic-fields/">High Magnetic Fields</a></h3>
    
    <ul>
      <li><a href="/browse/high-magnetic-fields/pulsed-magnets/">Pulsed Magnets</a></li>
      <li><a href="/browse/high-magnetic-fields/superconducting-magnets/">Superconducting Magnets</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/high-throughput-screening/">High Throughput Screening</a></h3>
    
    <ul>
      <li><a href="/browse/high-throughput-screening/imaging/">Imaging</a></li>
      <li><a href="/browse/high-throughput-screening/liquid-handling/">Liquid Handling</a></li>
      <li><a href="/browse/high-throughput-screening/plate-feeder/">Plate Feeder</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/histology/">Histology</a></h3>
    
    <ul>
      <li><a href="/browse/histology/cryosectioning/">Cryosectioning</a></li>
      <li><a href="/browse/histology/embedding-and-tissue-processing/">Embedding and Tissue Processing</a></li>
      <li><a href="/browse/histology/laser-capture-microdissection/">Laser Capture Microdissection</a></li>
      <li><a href="/browse/histology/microtomy/">Microtomy</a></li>
      <li><a href="/browse/histology/tissue-microarrayer/">Tissue Microarrayer</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/imaging/">Imaging</a></h3>
    
    <ul>
      <li><a href="/browse/imaging/angiography/">Angiography</a></li>
      <li><a href="/browse/imaging/blood-flow-imaging/">Blood flow imaging</a></li>
      <li><a href="/browse/imaging/calcium-imaging-system/">Calcium imaging system</a></li>
      <li><a href="/browse/imaging/camera/">Camera</a></li>
      <li><a href="/browse/imaging/camera-trap/">Camera Trap</a></li>
      <li><a href="/browse/imaging/computed-tomography/">Computed tomography</a></li>
      <li><a href="/browse/imaging/confocal-microscope/">Confocal Microscope (Laser Scanning)</a></li>
      <li><a href="/browse/imaging/confocal-imaging-system/">Confocal imaging system</a></li>
      <li><a href="/browse/imaging/crystal-imaging/">Crystal Imaging</a></li>
      <li><a href="/browse/imaging/digital-tem-camera/">Digital TEM Camera</a></li>
      <li><a href="/browse/imaging/echocardiography/">Echocardiography</a></li>
      <li><a href="/browse/imaging/electromagnetic-acoustic-imaging/">Electromagnetic Acoustic Imaging</a></li>
      <li><a href="/browse/imaging/electron-backscatter-diffraction/">Electron Backscatter Diffraction (EBSD) Camera</a></li>
      <li><a href="/browse/imaging/focused-ion-beam/">Focused Ion Beam (FIB)</a></li>
      <li><a href="/browse/imaging/gel-documentation-and-or-molecular-imaging/">Gel Documentation and/or Molecular Imaging</a></li>
      <li><a href="/browse/imaging/high-content-screening/">High Content Screening</a></li>
      <li><a href="/browse/imaging/high-throughput-tomographic-imaging/">High throughput tomographic imaging</a></li>
      <li><a href="/browse/imaging/imaging/">Imaging</a></li>
      <li><a href="/browse/imaging/intravascular-ultrasound/">Intravascular Ultrasound (IVUS)</a></li>
      <li><a href="/browse/imaging/magnetic-resonance-imaging/">Magnetic Resonance Imaging (MRI)</a></li>
      <li><a href="/browse/imaging/magnetic-resonance-imaging-spectroscopy/">Magnetic Resonance Imaging / Spectroscopy (MRI/MRS)</a></li>
      <li><a href="/browse/imaging/microscope/">Microscope</a></li>
      <li><a href="/browse/imaging/other/">Other</a></li>
      <li><a href="/browse/imaging/stereology/">Stereology</a></li>
      <li><a href="/browse/imaging/ultrasonography/">Ultrasonography</a></li>
      <li><a href="/browse/imaging/video-camera/">Video Camera</a></li>
      <li><a href="/browse/imaging/viewing-angle-instrumentation/">Viewing Angle Instrumentation</a></li>
      <li><a href="/browse/imaging/x-ray-microtomography/">X-ray Microtomography (Micro-CT)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/laser/">Laser</a></h3>
    
    <ul>
      <li><a href="/browse/laser/dye-laser/">Dye Laser</a></li>
      <li><a href="/browse/laser/excimer-laser/">Excimer Laser</a></li>
      <li><a href="/browse/laser/femtosecond-laser/">Femtosecond Laser</a></li>
      <li><a href="/browse/laser/laser-ablation/">Laser Ablation</a></li>
      <li><a href="/browse/laser/stent-cutting/">Stent Cutting</a></li>
      <li><a href="/browse/laser/supercontinuum-source/">Supercontinuum Source</a></li>
      <li><a href="/browse/laser/ultrafast-amplifier/">Ultrafast Amplifier</a></li>
      <li><a href="/browse/laser/ultrafast-oscillator/">Ultrafast Oscillator</a></li>
      <li><a href="/browse/laser/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/liquid-sample-handling/">Liquid / Sample Handling</a></h3>
    
    <ul>
      <li><a href="/browse/liquid-sample-handling/automated-workstation/">Automated Workstation</a></li>
      <li><a href="/browse/liquid-sample-handling/blood-reformatting/">Blood Reformatting</a></li>
      <li><a href="/browse/liquid-sample-handling/crystal-handling/">Crystal Handling</a></li>
      <li><a href="/browse/liquid-sample-handling/liquid-handling/">Liquid Handling</a></li>
      <li><a href="/browse/liquid-sample-handling/pipetting/">Pipetting</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/macromolecule-particle-characterisation/">Macromolecule / Particle Characterisation</a></h3>
    
    <ul>
      <li><a href="/browse/macromolecule-particle-characterisation/differential-sedimentation/">Differential Sedimentation</a></li>
      <li><a href="/browse/macromolecule-particle-characterisation/dynamic-light-scattering/">Dynamic Light Scattering</a></li>
      <li><a href="/browse/macromolecule-particle-characterisation/engine-particulate-analyzer/">Engine Particulate Analyzer</a></li>
      <li><a href="/browse/macromolecule-particle-characterisation/mie-scattering/">Mie Scattering</a></li>
      <li><a href="/browse/macromolecule-particle-characterisation/multi-angle-light-scattering/">Multi-Angle Light Scattering (MALS)</a></li>
      <li><a href="/browse/macromolecule-particle-characterisation/nanoparticle-tracking-analysis/">Nanoparticle Tracking Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/magnetic-properties/">Magnetic Properties</a></h3>
    
    <ul>
      <li><a href="/browse/magnetic-properties/magnetic-thermal-and-electrical-measurement/">Magnetic, Thermal and Electrical Measurement</a></li>
      <li><a href="/browse/magnetic-properties/squid-magnetometry/">SQUID Magnetometry</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/mass-spectrometry/">Mass Spectrometry (MS)</a></h3>
    
    <ul>
      <li><a href="/browse/mass-spectrometry/esi-tof-ms/">ESI-TOF MS</a></li>
      <li><a href="/browse/mass-spectrometry/inductively-coupled-plasma-ms/">Inductively Coupled Plasma MS (ICP-MS)</a></li>
      <li><a href="/browse/mass-spectrometry/ion-trap-ms/">Ion Trap MS</a></li>
      <li><a href="/browse/mass-spectrometry/isotope-ratio-ms/">Isotope Ratio MS</a></li>
      <li><a href="/browse/mass-spectrometry/linear-trap-orbitrap-ms/">Linear Trap / Orbitrap MS</a></li>
      <li><a href="/browse/mass-spectrometry/maldi-ms/">MALDI MS</a></li>
      <li><a href="/browse/mass-spectrometry/maldi-tof-ms/">MALDI-TOF MS</a></li>
      <li><a href="/browse/mass-spectrometry/maldi-tof-tof-ms/">MALDI-TOF/TOF MS</a></li>
      <li><a href="/browse/mass-spectrometry/radiocarbon-dating/">Radiocarbon Dating </a></li>
      <li><a href="/browse/mass-spectrometry/sample-analysis/">Sample Analysis</a></li>
      <li><a href="/browse/mass-spectrometry/secondary-ion-ms/">Secondary Ion MS (SIMS)</a></li>
      <li><a href="/browse/mass-spectrometry/tof-ms/">TOF MS</a></li>
      <li><a href="/browse/mass-spectrometry/thermal-ionization-ms/">Thermal Ionization MS (TIMS)</a></li>
      <li><a href="/browse/mass-spectrometry/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/materials-testing/">Materials Testing</a></h3>
    
    <ul>
      <li><a href="/browse/materials-testing/extrusion/">Extrusion</a></li>
      <li><a href="/browse/materials-testing/oxygen-permeability/">Oxygen Permeability</a></li>
      <li><a href="/browse/materials-testing/rheometry/">Rheometry</a></li>
      <li><a href="/browse/materials-testing/strain-measurement/">Strain Measurement </a></li>
      <li><a href="/browse/materials-testing/tensile-testing/">Tensile Testing</a></li>
      <li><a href="/browse/materials-testing/unspecified/">Unspecified</a></li>
      <li><a href="/browse/materials-testing/water-vapour-permeability/">Water Vapour Permeability</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/mechanical-testing/">Mechanical Testing</a></h3>
    
    <ul>
      <li><a href="/browse/mechanical-testing/microindentation/">Microindentation</a></li>
      <li><a href="/browse/mechanical-testing/nanoindentation/">Nanoindentation</a></li>
      <li><a href="/browse/mechanical-testing/nanomechanical-testing/">Nanomechanical Testing</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/micro-ct/">Micro CT</a></h3>
    
    <ul>
      <li><a href="/browse/micro-ct/in-vivo-x-ray-microtomography/">in vivo X-ray microtomography (Micro CT)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/microarrays/">Microarrays</a></h3>
    
    <ul>
      <li><a href="/browse/microarrays/microarray-processing/">Microarray Processing</a></li>
      <li><a href="/browse/microarrays/microarray-scanning/">Microarray Scanning</a></li>
      <li><a href="/browse/microarrays/microarrayer/">Microarrayer</a></li>
      <li><a href="/browse/microarrays/scanning-automation/">Scanning Automation</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/microbial-detection/">Microbial Detection</a></h3>
    
    <ul>
      <li><a href="/browse/microbial-detection/blood-culture-system/">Blood Culture System</a></li>
      <li><a href="/browse/microbial-detection/mycobacterial-detection/">Mycobacterial Detection </a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/microscale-thermophoresis/">Microscale Thermophoresis</a></h3>
    
    <ul>
      <li><a href="/browse/microscale-thermophoresis/other/">Other</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/microscopy/">Microscopy</a></h3>
    
    <ul>
      <li><a href="/browse/microscopy/atom-probe-microscopy/">Atom Probe Microscopy</a></li>
      <li><a href="/browse/microscopy/atomic-force-microscopy/">Atomic Force Microscopy (AFM)</a></li>
      <li><a href="/browse/microscopy/confocal-microscope/">Confocal Microscope</a></li>
      <li><a href="/browse/microscopy/confocal-microscopy/">Confocal Microscopy</a></li>
      <li><a href="/browse/microscopy/dental-microscopy/">Dental Microscopy</a></li>
      <li><a href="/browse/microscopy/fluorescence-microscopy/">Fluorescence Microscopy</a></li>
      <li><a href="/browse/microscopy/focused-ion-beam-scanning-electron-microscopy/">Focused Ion Beam-Scanning Electron Microscopy (FIB-SEM)</a></li>
      <li><a href="/browse/microscopy/microscopy/">Microscopy</a></li>
      <li><a href="/browse/microscopy/multi-photon-microscope/">Multi photon Microscope</a></li>
      <li><a href="/browse/microscopy/multiphoton-microscopy/">Multiphoton Microscopy</a></li>
      <li><a href="/browse/microscopy/optical-microscopy/">Optical Microscopy</a></li>
      <li><a href="/browse/microscopy/scanning-acoustic-microscopy/">Scanning Acoustic Microscopy (SAM)</a></li>
      <li><a href="/browse/microscopy/scanning-electron-microscopy/">Scanning Electron Microscopy (SEM)</a></li>
      <li><a href="/browse/microscopy/scanning-probe-microscopy/">Scanning Probe Microscopy (SPM)</a></li>
      <li><a href="/browse/microscopy/stereomicroscopy/">Stereomicroscopy</a></li>
      <li><a href="/browse/microscopy/surgical-microscopy/">Surgical Microscopy</a></li>
      <li><a href="/browse/microscopy/transmission-electron-microscopy/">Transmission Electron Microscopy (TEM)</a></li>
      <li><a href="/browse/microscopy/virtual-slide-scanner/">Virtual Slide Scanner</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/neurological-response/">Neurological Response</a></h3>
    
    <ul>
      <li><a href="/browse/neurological-response/eeg-and-fmri-amplifier/">EEG and fMRI amplifier </a></li>
      <li><a href="/browse/neurological-response/electroencephalography/">Electroencephalography (EEG)</a></li>
      <li><a href="/browse/neurological-response/eye-tracking/">Eye Tracking</a></li>
      <li><a href="/browse/neurological-response/magnetoencephalography/">Magnetoencephalography (MEG)</a></li>
      <li><a href="/browse/neurological-response/pain-response/">Pain Response</a></li>
      <li><a href="/browse/neurological-response/transcranial-magnetic-stimulation/">Transcranial Magnetic Stimulation (TMS)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/other/">Other</a></h3>
    
    <ul>
      <li><a href="/browse/other/3d-printer/">3D Printer</a></li>
      <li><a href="/browse/other/anaesthesia/">Anaesthesia</a></li>
      <li><a href="/browse/other/battery-tester/">Battery Tester</a></li>
      <li><a href="/browse/other/biobank/">Biobank</a></li>
      <li><a href="/browse/other/car/">Car</a></li>
      <li><a href="/browse/other/cleanroom/">Cleanroom</a></li>
      <li><a href="/browse/other/compound-storage-system/">Compound Storage System</a></li>
      <li><a href="/browse/other/controlled-environment-room/">Controlled Environment Room</a></li>
      <li><a href="/browse/other/coordinate-measuring-machine/">Coordinate Measuring Machine</a></li>
      <li><a href="/browse/other/deformable-mirror/">Deformable Mirror</a></li>
      <li><a href="/browse/other/electron-beam-lithography/">Electron Beam Lithography</a></li>
      <li><a href="/browse/other/electrophysiology/">Electrophysiology</a></li>
      <li><a href="/browse/other/engineering-machinery/">Engineering Machinery</a></li>
      <li><a href="/browse/other/fermentation/">Fermentation</a></li>
      <li><a href="/browse/other/freeze-drying/">Freeze Drying</a></li>
      <li><a href="/browse/other/frozen-archive-store/">Frozen Archive Store</a></li>
      <li><a href="/browse/other/geological/">Geological</a></li>
      <li><a href="/browse/other/glove-box/">Glove Box</a></li>
      <li><a href="/browse/other/greenhouse/">Greenhouse</a></li>
      <li><a href="/browse/other/helium-liquefaction-refrigerants/">Helium Liquefaction / Refrigerants</a></li>
      <li><a href="/browse/other/hemi-anechoic-chamber/">Hemi-Anechoic Chamber</a></li>
      <li><a href="/browse/other/hypoxia-workstation/">Hypoxia Workstation</a></li>
      <li><a href="/browse/other/intra-aortic-balloon-pump/">Intra-Aortic Balloon Pump</a></li>
      <li><a href="/browse/other/laser-scanner/">Laser Scanner</a></li>
      <li><a href="/browse/other/liquid-nitrogen-cryogenic-storage/">Liquid Nitrogen Cryogenic Storage</a></li>
      <li><a href="/browse/other/luminescence-dating/">Luminescence Dating</a></li>
      <li><a href="/browse/other/marine-water/">Marine Water</a></li>
      <li><a href="/browse/other/mechanical-design-and-analysis/">Mechanical Design and Analysis</a></li>
      <li><a href="/browse/other/media/">Media</a></li>
      <li><a href="/browse/other/microelectrode-array/">Microelectrode array</a></li>
      <li><a href="/browse/other/multiplex-analysis/">Multiplex Analysis</a></li>
      <li><a href="/browse/other/peptide-synthesis/">Peptide Synthesis</a></li>
      <li><a href="/browse/other/photofabrication/">Photofabrication</a></li>
      <li><a href="/browse/other/plant-growth/">Plant Growth</a></li>
      <li><a href="/browse/other/protein-preparation/">Protein Preparation</a></li>
      <li><a href="/browse/other/robot/">Robot</a></li>
      <li><a href="/browse/other/semiconductor-device-analyzer/">Semiconductor Device Analyzer</a></li>
      <li><a href="/browse/other/simulation/">Simulation</a></li>
      <li><a href="/browse/other/space-instruments/">Space Instruments</a></li>
      <li><a href="/browse/other/spray-drying/">Spray Drying</a></li>
      <li><a href="/browse/other/translation-stage/">Translation Stage</a></li>
      <li><a href="/browse/other/tube-decapping-recapping/">Tube Decapping / Recapping</a></li>
      <li><a href="/browse/other/unspecified/">Unspecified</a></li>
      <li><a href="/browse/other/ventilator/">Ventilator</a></li>
      <li><a href="/browse/other/virtual-reality/">Virtual Reality</a></li>
      <li><a href="/browse/other/wind-tunnel/">Wind Tunnel</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/plate-reader/">Plate Reader</a></h3>
    
    <ul>
      <li><a href="/browse/plate-reader/absorbance-microplate-reader/">Absorbance Microplate Reader</a></li>
      <li><a href="/browse/plate-reader/elispot-plate-reader/">ELISpot Plate Reader</a></li>
      <li><a href="/browse/plate-reader/multi-mode-microplate-reader/">Multi-Mode Microplate Reader</a></li>
      <li><a href="/browse/plate-reader/turbidity-microplate-reader/">Turbidity Microplate Reader</a></li>
      <li><a href="/browse/plate-reader/unspecified/">Unspecified</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/protein-peptide-id/">Protein/Peptide ID</a></h3>
    
    <ul>
      <li><a href="/browse/protein-peptide-id/hplc/">HPLC</a></li>
      <li><a href="/browse/protein-peptide-id/mass-spec/">Mass Spec</a></li>
      <li><a href="/browse/protein-peptide-id/uhplc/">UHPLC</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/purification/">Purification</a></h3>
    
    <ul>
      <li><a href="/browse/purification/sample-analysis/">Sample Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/radiometry/">Radiometry</a></h3>
    
    <ul>
      <li><a href="/browse/radiometry/gamma-counter/">Gamma Counter</a></li>
      <li><a href="/browse/radiometry/phosphorimaging/">Phosphorimaging</a></li>
      <li><a href="/browse/radiometry/scintillation-counting/">Scintillation Counting</a></li>
      <li><a href="/browse/radiometry/scintillation-and-luminescence-counting/">Scintillation and Luminescence Counting</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/sample-analysis/">Sample Analysis</a></h3>
    
    <ul>
      <li><a href="/browse/sample-analysis/hplc/">HPLC</a></li>
      <li><a href="/browse/sample-analysis/nmr/">NMR </a></li>
      <li><a href="/browse/sample-analysis/sample-analysis/">Sample Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/sample-prep/">Sample Prep</a></h3>
    
    <ul>
      <li><a href="/browse/sample-prep/centrifuge/">Centrifuge</a></li>
      <li><a href="/browse/sample-prep/evapouration/">Evapouration</a></li>
      <li><a href="/browse/sample-prep/incubator-shakers/">Incubator shakers</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/semiconductor/">Semiconductor</a></h3>
    
    <ul>
      <li><a href="/browse/semiconductor/tabletop-sem/">Tabletop SEM</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/sonication/">Sonication</a></h3>
    
    <ul>
      <li><a href="/browse/sonication/ultrasound/">Ultrasound</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/spectrometry/">Spectrometry</a></h3>
    
    <ul>
      <li><a href="/browse/spectrometry/stopped-flow/">Stopped Flow</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/spectrophotometer/">Spectrophotometer</a></h3>
    
    <ul>
      <li><a href="/browse/spectrophotometer/plate-reader/">Plate reader</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/spectroscopy/">Spectroscopy</a></h3>
    
    <ul>
      <li><a href="/browse/spectroscopy/circular-dichroism/">Circular Dichroism</a></li>
      <li><a href="/browse/spectroscopy/dynamic-nuclear-polarisation/">Dynamic Nuclear Polarisation (DNP) Nuclear Magnetic Resonance (NMR) </a></li>
      <li><a href="/browse/spectroscopy/electron-paramagnetic-resonance/">Electron Paramagnetic Resonance (EPR)</a></li>
      <li><a href="/browse/spectroscopy/electron-probe-microanalysis/">Electron Probe Microanalysis (EPMA)</a></li>
      <li><a href="/browse/spectroscopy/fluorescence-spectrometry/">Fluorescence Spectrometry</a></li>
      <li><a href="/browse/spectroscopy/fourier-transform-infrared/">Fourier Transform Infrared (FTIR) Spectrometry </a></li>
      <li><a href="/browse/spectroscopy/nuclear-magnetic-resonance/">Nuclear Magnetic Resonance (NMR)</a></li>
      <li><a href="/browse/spectroscopy/other/">Other</a></li>
      <li><a href="/browse/spectroscopy/raman-spectroscopy/">Raman Spectroscopy</a></li>
      <li><a href="/browse/spectroscopy/uv-vis-spectrometry/">UV-Vis Spectrometry </a></li>
      <li><a href="/browse/spectroscopy/uv-vis-spectroscopy/">UV-Vis Spectroscopy</a></li>
      <li><a href="/browse/spectroscopy/uv-vis-nir-spectrometry/">UV-Vis-NIR Spectrometry</a></li>
      <li><a href="/browse/spectroscopy/x-ray-fluorescence/">X-ray Fluorescence (XRF) Spectroscopy </a></li>
      <li><a href="/browse/spectroscopy/x-ray-photoelectron-spectroscopy/">X-ray Photoelectron Spectroscopy (XPS)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/surface-analysis-modification/">Surface Analysis / Modification</a></h3>
    
    <ul>
      <li><a href="/browse/surface-analysis-modification/ellipsometry/">Ellipsometry</a></li>
      <li><a href="/browse/surface-analysis-modification/form-and-roughness/">Form and Roughness</a></li>
      <li><a href="/browse/surface-analysis-modification/optical-profilometry/">Optical Profilometry</a></li>
      <li><a href="/browse/surface-analysis-modification/oxygen-plasma-etcher/">Oxygen Plasma Etcher</a></li>
      <li><a href="/browse/surface-analysis-modification/physisorption/">Physisorption</a></li>
      <li><a href="/browse/surface-analysis-modification/physisorption-and-chemisorption/">Physisorption and Chemisorption</a></li>
      <li><a href="/browse/surface-analysis-modification/polymer-processing/">Polymer Processing</a></li>
      <li><a href="/browse/surface-analysis-modification/reactive-ion-etching/">Reactive-Ion Etching (RIE)</a></li>
      <li><a href="/browse/surface-analysis-modification/stylus-profilometry/">Stylus Profilometry</a></li>
      <li><a href="/browse/surface-analysis-modification/surface-tension/">Surface Tension</a></li>
      <li><a href="/browse/surface-analysis-modification/thin-film-deposition/">Thin Film Deposition</a></li>
      <li><a href="/browse/surface-analysis-modification/ultra-high-vacuum/">Ultra-high Vacuum (UHV) Chamber</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/thermal-analysis-calorimetry/">Thermal Analysis / Calorimetry</a></h3>
    
    <ul>
      <li><a href="/browse/thermal-analysis-calorimetry/differential-scanning-calorimetry/">Differential Scanning Calorimetry (DSC)</a></li>
      <li><a href="/browse/thermal-analysis-calorimetry/dynamic-mechanical-analysis/">Dynamic Mechanical Analysis (DMA)</a></li>
      <li><a href="/browse/thermal-analysis-calorimetry/isothermal-titration-calorimetry/">Isothermal Titration Calorimetry</a></li>
      <li><a href="/browse/thermal-analysis-calorimetry/microcalorimetry/">Microcalorimetry</a></li>
      <li><a href="/browse/thermal-analysis-calorimetry/thermogravimetric-analysis/">Thermogravimetric Analysis (TGA)</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/thermoplastic-processing/">Thermoplastic Processing</a></h3>
    
    <ul>
      <li><a href="/browse/thermoplastic-processing/thermoplastic-modelling/">Thermoplastic Modelling</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/ultrasound/">Ultrasound</a></h3>
    
    <ul>
      <li><a href="/browse/ultrasound/ultrasonography/">Ultrasonography</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/western-blotting/">Western Blotting</a></h3>
    
    <ul>
      <li><a href="/browse/western-blotting/sample-analysis/">Sample Analysis</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/workshops/">Workshops</a></h3>
    
    <ul>
      <li><a href="/browse/workshops/electronics/">Electronics</a></li>
      <li><a href="/browse/workshops/glassblowing/">Glassblowing</a></li>
      <li><a href="/browse/workshops/mechanical/">Mechanical</a></li>
    </ul>
    
    
  </li>

  <li class="equipment-category">
    <h3><a href="/browse/qpcr/">qPCR</a></h3>
    
    <ul>
      <li><a href="/browse/qpcr/imaging/">Imaging</a></li>
    </ul>
    
    
  </li>

</ul>








      </div>
      </article>

    
  
      <aside class="left-sidebar">
        <nav>
          <h2 class="hidden">Site Navigation</h2>
          <ul>
            <li><a href="/">home</a></li>
            <li><a href="/search/">search</a></li>
            <li><a href="/browse/">browse by category</a></li>
            <li><a href="/facilities/">facilities</a></li>
            <li><a href="/departments/">departments</a></li>
            <li><a href="/about/">about</a></li>
            <li><a href="/contribute/">contribute</a></li>
            <li><a href="/contact/">contact</a></li>
            </ul>
            
            <div class="panel user" >
            
            <p class="iam">logged in as <span class="realName">Andrew Stretton</span> </p>
            <p class="logInOut">
            <a href="/accounts/logout/">log out</a></p>
            
          </div>
          
          <div class="equipment-credit">Supported by:
          <a href="http://www.epsrc.ac.uk/" class="brandmark" id="brandmark-epsrc" title="Work on this project has been facilitated by an EPSRC Institutional Sponsorship Grant (EPSRC Delivery Plan theme: ‘Efficiency and Effectiveness - promoting sharing of research equipment’)">Engineering and Physical Sciences Research Council</a>
          </div>

          <div class="equipment-credit">Powered by:
          <a href="https://data.ox.ac.uk/" class="brandmark" id="brandmark-open-data-service">University of Oxford Open Data Service</a>
          </div>
          
        </nav>
      </aside>
    
    
    <!-- close .main -->
    <div style="clear:both"></div>
    </div>

    <footer class="site">
      <div class="copyright">
         © University of Oxford
        
        <a href="/legal-and-privacy/">Privacy statement</a>

        <a href="http://www.oucs.ox.ac.uk/infodev/">Site by InfoDev, IT Services</a>
      <!-- close .copyright -->
      </div>
    </footer>
    </div><!-- /end #page -->
  
<script type="text/javascript" src="//active.oucs.ox.ac.uk/shared/stylesheet/js/jquery.cookie.js"></script>
<script type="text/javascript" src="//active.oucs.ox.ac.uk/shared/stylesheet/analytics/analytics.js"></script>
<script type="text/javascript">
  optionalAnalytics({
    analyticsID: "UA\u002D32168758\u002D1",
    domain: "www.research\u002Dfacilities.ox.ac.uk",
    doNotTrack: false,
    privacyPolicyURL: "//www.research\u002Dfacilities.ox.ac.uk/legal\u002Dand\u002Dprivacy/#analytics",
    policy: "out-out",
    bannerText: "We would like to use cookies to collect data on how people use our site. Analytics cookies are currently being set, which you can <a href=\"analytics-reject\">disable</a>. If you're happy for cookies to continue to be set, you may <a id=\"analytics-accept\">dismiss this notice</a>. See our <a id=\"analytics-policy\">cookie policy</a> for more information, and to change your preference later.",
          extraGaq: [["_setCustomVar", 1, "authenticated", "yes", 2], ["_setCustomVar", 2, "status", "staff", 1], ["_setCustomVar", 3, "affiliation", "chembio,sgc", 1]]
  });
</script>


</body>
</html>

"""

soup = BeautifulSoup(page, 'html.parser')

items = []
import json
for li in soup.select(".equipment-category"):
    group = li.h3.text
    items.append({"group" : group, "label" : group + " (all)", "value": group })
    for lin in li.ul:
        if lin.string.strip():
             items.append({"group" : group, "label": lin.string.strip(), "value": lin.string.strip()})

print json.dumps(items)









#copy (select array_to_json(array_agg(row_to_json(t)))  from (select  array_to_string( array[l1,l2,l3,l4,l5,l6,l7,l8 ], ' >> ') as group , target_dictionary.pref_name as label, target_dictionary.chembl_id as value,  b.descr as description from  (select component_class.component_id as cid, string_agg(component_synonyms.component_synonym,', ') as descr from protein_family_classification left join component_class on protein_family_classification.protein_class_id=component_class.protein_class_id left join component_sequences on component_sequences.component_id = component_class.component_id left join component_synonyms on component_class.component_id=component_synonyms.component_id  where component_type='PROTEIN' group by component_class.component_id ) as b inner join target_components on cid=target_components.component_id inner join target_dictionary on target_components.tid = target_dictionary.tid  left join component_sequences on component_sequences.component_id=cid left join component_class on component_class.component_id = cid left join protein_family_classification on protein_family_classification.protein_class_id=component_class.protein_class_id ) as  t) to '/tmp/targets.json' ;

#copy (select array_to_json(array_agg(row_to_json(t))) from (select   array_to_string( array[l1,l2,l3,l4,l5,l6,l7,l8 ], ' >> ') as description, (case when l8 is not null then l8  when l7 is not null then l7 when l6 is not null then l6 when l5 is not null then l5 when l4 is not null then l4 when l3 is not null then l3 when l2 is not null then l2 else l1 end) as value, (case when l8 is not null then l8  when l7 is not null then l7 when l6 is not null then l6 when l5 is not null then l5 when l4 is not null then l4 when l3 is not null then l3 when l2 is not null then l2 else l1 end) as label, l1 as group from protein_family_classification ) as t ) to '/tmp/families.json';
