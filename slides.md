% title: Inferring protein structure and dynamics from simulation and experiment
% author: Kyle A. Beauchamp
% author: Das and Pande Labs

---
title: Biological Macromolecules

<table width="100%">
 <tr>
  <td width="33%"><img height=400 src=figures/4bna.png /></td>
  <td width="33%"><img height=400 src=figures/1zih.png /></td>
  <td width="33%"><img height=400 src=figures/2hbb.png /></td>
 </tr>
</table>

<footer class="source"> Dickerson, 1988; Pardi, 1996; Raleigh, 2007  </footer>

---
title: Atomic Perturbations and Disease

...EVKMD<b><font color="black">A</font></b>EFRHDS...  ...EVKMD<b><font color="black">T</font></b>EFRHDS...  ...EVKMD<b><font color="black">V</font></b>EFRHDS...

<img width=300 src=figures/alanine.png />  <img width=300 src=figures/threonine.png />   <img width=300 src=figures/valine.png />

<img width=300 src=figures/sick.png />  <img width=300 src=figures/healthy.png />   <img width=300 src=figures/sicker.png />

<footer class="source"> Jonsson, 2012  </footer>

---
title: Molecular Medicine

<img width=475 src=figures/tiotropium.png /> <img width=425 src=figures/4daj.png />

<footer class="source"> Wikipedia; Kobilka, 2012  </footer>

---
title: Protein Folding

<img width=475 src=figures/tiotropium.png /> <img width=425 src=figures/4daj.png />

<footer class="source"> Wikipedia; Kobilka, 2012  </footer>

---
title: Goal: Predictive, atomic-detail models of protein structure and dynamics (and folding!)
class: segue dark nobackground

---
title: What do we know about macromolecules?

<img heigh=200 src=figures/crystal.jpg />  <img height=200 src=figures/HP35_CD.png />  <img height=200 src=figures/HP35_relaxation.png /> 

---
title: What do macromolecules look like?

Structural biology provides atomic-scale models of <i>selected</i> conformational states.
<center>
<img width=500 src=figures/crystal.jpg /> 
</center>

<footer class="source"> http://cbic.yale.edu/crystallization-automation </footer>

---
title: How do macromolecules work?
subtitle: Biophysical experiments characterize equilibrium and kinetic properties along <i>selected</i> order parameters.

<img height=300 src=figures/HP35_CD.png />  <img height=300 src=figures/HP35_relaxation.png /> 

---
title: Limitations of current measurements

- One protein (condition), one structure
- Unnatural or perturbative sample conditions
- Limited structural and temporal resolution 
- Interpreting / integrating data from multiple experiments


---
title: Introduction to Atomistic Simulation
class: segue dark nobackground

---
title: Molecular Dynamics

- Simulate the physical interactions of proteins in solution
- Numerically integrate the equations of motion

<center>
<img height=430 src=figures/hp35_box.png />
</center>

---
title: 100 $\mu s$ of HP35 Dynamics
<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_shaw.ogv" type="video/ogg">
</video>
</center> 

<footer class="source"> 
Shaw, 2011
</footer>

---
title: Goals of Atomistic Simulation

- Calculate experimental observables
- Interpret experimental observables
- Generate atomic-detail hypotheses

---
title: Challenges in Molecular Simulation

- Sampling biologically-relevant timescales
- Meaningful connection to experiment
- Limited forcefield accuracy

<center>
<img height=350 src=figures/protein_timescales.jpg />
</center>

---
title: Outline

- Inferring Protein Dynamics from Molecular Simulation
- Quantitative Comparison of villin headpiece simulations and Triple-Triplet Energy Transfer Experiments
- Inferring Conformational Ensembles from Noisy Experiments

---
title: Inferring Protein Dynamics from Molecular Simulation
class: segue dark nobackground

---
title: Two Challenges in Molecular Simulation
subtitle: How to sample biological timescales?

<img height=300 src=figures/anton.jpg />  <img height=300 src=figures/TitanNew.jpg />

<footer class="source"> 
Shaw et al.  , Eastman et. al.,  NVIDIA / Anandtech.  
</footer>

---
title: Two Challenges in Molecular Simulation
subtitle: Connecting to experiment

<img height=300 src=figures/hp35_box.png />   <img height=300 src=figures/HP35_relaxation.png />   <img height=300 src=figures/folding_reaction.png />

---
title: Markov State Models

- Run parallel simulations on commodity hardware
- Build kinetic model of dynamics
- Quantitive model of structure, equilibrium, and kinetics

<img height=250 src=figures/hp35_box.png /> <img height=250 src=figures/NTL9_network.jpg />   <img height=250 src=figures/HP35_relaxation.png />

<footer class="source"> 
Bowman, Beauchamp, Boxer, Pande, 2009. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Voelz, Bowman, Beauchamp, Pande, 2010.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Beauchamp, Bowman, Lane, Maibaum, Haque, Pande 2011. <br>
Beauchamp, McGibbon, Lin, Pande, 2012. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Also: Chodera, Huang, Noe, Hummer, Dill, and others.
</footer>

---
title: 100 $\mu s$ of HP35 Dynamics (MSM)

<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_msm.ogv" type="video/ogg">
</video>
</center> 

<footer class="source"> 
<br>
Beauchamp, K. A., Ensign, D. L., Das, R., & Pande, V. S.  PNAS 2011.
</footer>

---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths1.png />
</center>
---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths2.png />
</center>


---
title: Introduction to Markov State Models

<center>
<img height=400 src=figures/NewPaths3.png />
</center>


---
title: Counting Transitions

<center>
$A = (1112222)$

$\downarrow$

$C = \begin{pmatrix}2 & 1 \\\ 0 & 3\end{pmatrix}$

</center>

---
title: Estimating Rates

<center>
$C = \begin{pmatrix}2 & 1 \\\ 0 & 3\end{pmatrix}$

$\downarrow$

$T = \begin{pmatrix}\frac{2}{3} & \frac{1}{3} \\\ 0 & 1\end{pmatrix}$

</center>

---
title: MSMBuilder

<img height=400 src=figures/msmbuilder.png />  <img height=400 src=figures/msmb_users.png />

<footer class="source">
Contributions from Greg Bowman, Xuhui Huang, John Chodera, Sergio Bacallado, Dan Ensign, Vince Voelz, TJ Lane, Lutz Maibaum, Imran Haque, Robert McGibbon, Christian Schwantes, Toni Giorgino, Gianni de Fabritiis
</footer>

---
title: Progress in MSM Construction
subtitle: Scaling to full protein systems

<center>
<img height=400 src=figures/JCP_cover.jpg/>
</center>


<footer class="source">
Bowman, G. R., Beauchamp, K. A., Boxer, G., & Pande, V. S. (2009). Progress and challenges in the automated construction of Markov state models for full protein systems. The Journal of chemical physics, 131, 124101.
</footer>

---
title: Progress in MSM Construction
subtitle: Reaching millisecond timescales

<center>
<img height=400 src=figures/NTL9_network.jpg />
</center>

<footer class="source">
Voelz, V. A., Bowman, G. R., Beauchamp, K., & Pande, V. S. (2010). Molecular simulation of ab initio protein folding for a millisecond folder NTL9 (1− 39). Journal of the American Chemical Society, 132(5), 1526-1528.
</footer>

---
title: Progress in MSM Construction
subtitle: Algorithms for Accurate MSMs

<center>
<img height=300 src=figures/KCentersCentrality.png />  <img height=300 src=figures/HybridCentrality.png />  <img height=300 src=figures/TwoState-Pops.png />
</center>

<footer class="source">
Beauchamp, K. A., Bowman, G. R., Lane, T. J., Maibaum, L., Haque, I. S., & Pande, V. S. (2011). MSMBuilder2: Modeling conformational dynamics on the picosecond to millisecond scale. Journal of chemical theory and computation, 7(10), 3412-3419.
</footer>

---
title: Progress in MSM Construction
subtitle: Reconciling two and multi-state behavior in protein folding

<center>
<img height=400 src=figures/rate_spectra.png />
</center>

<footer class="source">
Beauchamp, K. A., McGibbon, R., Lin, Y. S., & Pande, V. S. (2012). Simple few-state models reveal hidden complexity in protein folding. Proceedings of the National Academy of Sciences, 109(44), 17807-17813.
</footer>

---
title: Quantitative Comparison of villin headpiece simulations and Triple-Triplet Energy Transfer Experiments
class: segue dark nobackground

---
title: HP35: A Model for Protein Folding


<center>
<img height=500 src=figures/hp35.png />
</center>


---
title: Triplet Triplet Energy Transfer

- Like FRET, but sensitive at the Angstrom level 
- Used to monitor rates of contact formation
- With denaturant, can probe native and unfolded states

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Structure-23-35.png />
</center>

<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Structure-1-35.png />
</center>


<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Triplet Triplet Energy Transfer

<center>
<img height=500 src=figures/Trace-1-35.png />
</center>


<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Simulating TTET in Silico
subtitle: A modified MSM can predict the output of TTET experiments

<center>
<img height=430 src=figures/ConformationalMSM.png />  <img height=450 src=figures/ElectronicMSM-full.png />
</center>


---
title: Measured TTET
subtitle: Kiefhaber measured four pairs of TTET probe locations

<center>
<img height=430 src=figures/AllTraces-Expt.png />
</center>

---
title: Comparing Simulation and Experiment

<center>
<img height=250 src=figures/AllTraces-Expt.png /> 

<img height=250 src=figures/AllTraces-MSM.png />

</center>


---
title: Predicting All TTET Experiments
subtitle: Robust to forcefield

<center>

<img height=420 src=figures/AllTTET-10424.png />  <img height=420 src=figures/AllTTET-3036.png />

</center>

<footer class="source">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff99sb-ildn
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff03
</footer>
---
title: Inferring Conformational Ensembles from Noisy Experiments
class: segue dark nobackground

---
title: Acknowledgements
subtitle: Rhiju and Vijay

---
title: Acknowledgements
subtitle: Das and Pande Labs

- Pablo Cordero
- Fang-Chieh Chou
- Parin Sripakdeevong

---
title: Acknowledgements
subtitle: MSMBuilder

- Greg Bowman
- Robert McGibbon
- Christian Schwantes
- TJ Lane
- Imran Haque
- Sergio Bacallado
- Lutz Maibaum
- Lee-Ping Wang

---
title: Acknowledgements
subtitle: TTET
Buzz Baldwin, Thomas Kiefhaber, Dan Herschlag


LVBP: John Chodera, Frank Cochran, TJ Lane

