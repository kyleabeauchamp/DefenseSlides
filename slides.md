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
title: The Atomistic Basis of Disease

...EVKMD<b><font color="black">A</font></b>EFRHDS...  ...EVKMD<b><font color="black">T</font></b>EFRHDS...  ...EVKMD<b><font color="black">V</font></b>EFRHDS...

<img width=300 src=figures/alanine.png />  <img width=300 src=figures/threonine.png />   <img width=300 src=figures/valine.png />

<footer class="source"> 
Jonsson, 2012  A673 T673 V673
</footer>

---
title: A crisis at the atomic scale

<center>
<img width=700 src=figures/length_scales_kyle.png />
</center>

<footer class="source"> 
http://www.nature.com/scitable/topicpage/what-is-a-cell-14023083
</footer>


---
title: Goal: Predictive, atomic-detail models of protein structure and dynamics
class: segue dark nobackground


---
title: Introduction to Molecular Dynamics

- Simulate the physical interactions of proteins in solution
- Numerically integrate the equations of motion

<center>
<img height=430 src=figures/hp35_box.png />
</center>

---
title: 100 $\mu s$ of HP35 Dynamics

<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_shaw.mp4" type="video/mp4">
</video>
</center> 

<footer class="source"> 
Shaw, 2011
</footer>

---
title: Goals of Atomistic Simulation

- Calculate experimental observables
- Generate atomic-detail hypotheses
- Interpret experimental observables

<center>
<img height=325 src=figures/hp35_box.png />  <img height=325 src=figures/HP35_relaxation.png />
</center>

<footer class="source"> 
Eaton, 2006
</footer>

---
title: Outline

- Inferring Protein Dynamics from Molecular Simulation
- Quantitative Comparison of Villin Headpiece Simulations and Triple-Triplet Energy Transfer Experiments
- Inferring Conformational Ensembles from Noisy Experiments

<center>
<img height=220 src=figures/NTL9_network.jpg />   <img height=220 src=figures/Structure2-7-23.png /> <img height=220 src=figures/ALA3_rama_amber96_belt.png />
</center>


---
title: Inferring Protein Dynamics from Molecular Simulation
class: segue dark nobackground

---
title: Two Challenges in Molecular Simulation
subtitle: How to sample biological timescales?

<center>
<img height=450 src=figures/protein_timescales.jpg />
</center>

<footer class="source">
Church, 2011.
</footer>

---

title: Two Challenges in Molecular Simulation
subtitle: How to sample biological timescales?

<img height=300 src=figures/anton.jpg />  <img height=300 src=figures/TitanNew.jpg />

<footer class="source"> 
Shaw et al.  , Eastman et. al.,  NVIDIA / Anandtech.  
</footer>

---

title: Two Challenges in Molecular Simulation
subtitle: Meaningful Connection to experiment

<img height=300 src=figures/hp35_box.png />   <img height=300 src=figures/HP35_relaxation.png />   <img height=300 src=figures/folding_reaction.png />

<footer class="source"> 
Eaton, 2006
</footer>

---
title: Markov State Models

- Run many parallel simulations on commodity hardware
- Build kinetic network model of dynamics
- Quantitively predict structure, equilibrium, and kinetics

<img height=250 src=figures/hp35_box.png /> <img height=250 src=figures/NTL9_network.jpg />   <img height=250 src=figures/HP35_relaxation.png />

<footer class="source"> 
Bowman, Beauchamp, Boxer, Pande, 2009. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Voelz, Bowman, Beauchamp, Pande, 2010.  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Beauchamp, Bowman, Lane, Maibaum, Haque, Pande 2011. <br>
Beauchamp, McGibbon, Lin, Pande, 2012. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Also: Chodera, Huang, Noé, Hummer, Dill, and others.
</footer>

---
title: 100 $\mu s$ of HP35 Dynamics (MSM)

<center>
<video width="640" height="480" controls>
  <source src="movies/hp35_msm.mp4" type="video/mp4">
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

<img height=300 src=figures/NewPaths-2State.png />

$\downarrow$

$A = (111222222)$

---
title: Counting Transitions

<center>

$A = (111222222)$

$\downarrow$

$C = \begin{pmatrix} C_{1\rightarrow 1} & C_{1\rightarrow 2} \\\ C_{2 \rightarrow 1} & C_{2 \rightarrow 2} \end{pmatrix} =  \begin{pmatrix}2 & 1 \\\ 0 & 5\end{pmatrix}$

</center>

---
title: Estimating Rates

<center>
$C = \begin{pmatrix} C_{1\rightarrow 1} & C_{1\rightarrow 2} \\\ C_{2 \rightarrow 1} & C_{2 \rightarrow 2} \end{pmatrix} = \begin{pmatrix}2 & 1 \\\ 0 & 5\end{pmatrix}$

$\downarrow$

$T = \begin{pmatrix} T_{1\rightarrow 1} & T_{1\rightarrow 2} \\\ T_{2 \rightarrow 1} & T_{2 \rightarrow 2} \end{pmatrix} = \begin{pmatrix}\frac{2}{3} & \frac{1}{3} \\\ 0 & 1\end{pmatrix}$

</center>

---
title: MSMBuilder
subtitle: An Open-Source, High-Performance, Python toolkit for MSM Construction

<img height=400 src=figures/msmbuilder.png />  <img height=400 src=figures/msmb_users.png />

<footer class="source">
Contributions from Greg Bowman, Xuhui Huang, John Chodera, Sergio Bacallado, Dan Ensign, Vince Voelz, TJ Lane, Lutz Maibaum, Imran Haque, Robert McGibbon, Christian Schwantes, Toni Giorgino, Gianni de Fabritiis
</footer>

---
title: Progress in MSM Construction
subtitle: Scaling to full protein systems

<center>
<img height=400 src=figures/JCP_cover.png />
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
<img height=350 src=figures/KCentersCentrality.png />  <img height=350 src=figures/HybridCentrality.png />
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
title: Quantitative Comparison of Villin Headpiece Simulations and Triple-Triplet Energy Transfer Experiments
class: segue dark nobackground

---
title: HP35: A Model for Protein Folding


<center>
<img height=500 src=figures/hp35.png />
</center>

<footer class="source"> Kim, Eaton, McKnight, Raleigh, others  </footer>

---
title: Triplet Triplet Energy Transfer

- Like FRET, but sensitive at the Å scale 
- Used to monitor rates of contact formation

<center>
<img height=225 src=figures/contact_formation.jpg />
</center>

<footer class="source">
Lapidus, 2000
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
title: Observed TTET at 4 probe locations

<center>
<img height=430 src=figures/AllTraces-Expt.png />
</center>

<footer class="source">
Kiefhaber, 2010.
</footer>

---
title: Simulating TTET in Silico
subtitle: A modified MSM can predict the output of TTET experiments

<center>
<img height=400 src=figures/ConformationalMSM.png /> <img height=420 src=figures/ElectronicMSM-full.png />
</center>

<footer class="source"> 
Beauchamp, K. A., Ensign, D. L., Das, R., & Pande, V. S.  PNAS 2011.
</footer>

---
title: TTET at positions (7,23)

<center>
<img height=400 src=figures/Structure2-7-23.png />
</center>

---
title: TTET at positions (7, 23)

<center>
<img height=500 src=figures/Data-7-23.png />
</center>

---
title: TTET at positions (1, 23)

<center>
<img height=400 src=figures/Structure2-1-23.png />
</center>

---
title: TTET at positions (1, 23)

<center>
<img height=500 src=figures/Data-1-23.png />
</center>

---
title: TTET at positions (23, 35)

<center>
<img height=400 src=figures/Structure2-23-35.png />
</center>

---
title: TTET at positions (23, 35)

<center>
<img height=500 src=figures/Data-23-35.png />
</center>

---
title: TTET at positions (1, 35)

<center>
<img height=400 src=figures/Structure2-1-35.png />
</center>

---
title: TTET at positions (1, 35)

<center>
<img height=500 src=figures/Data-1-35.png />
</center>

---
title: Predicting All TTET Experiments

<center>

<img height=420 src=figures/AllTTET-10424.png />  <img height=420 src=figures/AllTTET-3036.png />

</center>

<footer class="source">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff99sb-ildn
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
ff03

<br>

Beauchamp, K. A., Ensign, D. L., Das, R., & Pande, V. S.  PNAS 2011.

</footer>
---
title: TTET Conclusions

- Experimental advances revealed multi-state kinetics in smallest protein system
- MSMs capture multi-state kinetics and recapitulate TTET measurements
- Detailed comparison of simulation and experiment reveals need for better forcefields and observables

<footer class="source"> 
Beauchamp, K. A., Ensign, D. L., Das, R., & Pande, V. S.  PNAS 2011.
</footer>

---
title: Inferring Conformational Ensembles from Noisy Experiments (and simulation)
class: segue dark nobackground

---
title: What if the force fields are broken?

<img height=500 src=figures/elephant.jpg />

<footer class="source">
http://newh2o.com/2012/11/02/gemstones-elephant-in-the-room-free-project/
</footer>

---
title: Conformational ensembles

- Structure + Equilibrium (not kinetics)
- Characterize the population of <b>every</b> conformation
- <b>Rigorous</b> connection to equilibrium measurements

<center>
<img height=250 src=figures/model_hist0.png />  <img height=250 src=figures/ALA3_rama_amber96_raw.png />  <img height=250 src=figures/bpti_raw.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David_Covered.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David_statue.png />
</center>

---
title: Experiments as Projections

<center>
<img height=525 src=figures/David.png />
</center>

<footer class="source">
Regarded from two sides.  Diet Wiegman, 1984.
</footer>
---
title: Two Models, Same "Data"

<center>
<img height=500 src=figures/david_michelangelo.png /> <img height=500 src=figures/david_metal.png /> 
</center>

---
title: A Third Possibility

<center>
<img height=500 src=figures/david_michelangelo.png />  <img height=500 src=figures/harpoon.png />  <img height=500 src=figures/david_metal.png /> 
</center>


---
title: Ambiguous Measurements

<center>
<img height=500 src=figures/single_karplus.png />
</center>

---
title: Bayesian Energy Landscape Tilting 

- Infer conformational ensembles from simulation <b>and</b> ambiguous experiments
- Simulataneously model structure and population
- Characterize posterior through MCMC
- Error bars on equilibrium <b>and</b> structural features

<footer class="source"> 
Beauchamp, Das, Pande.  Inferring Structural Ensembles from Noisy Experiments: Application to Trialanine.  In Prep.
</footer>
---
title: Ingredients for Ensemble Inference

- Equilibrium molecular dynamics simulation, with conformations $x_j$
- Equilibrium experimental measurements $F_i$ with uncertainties $\sigma_i$
- Predicted experimental observables: $f_i(x)$

<footer class="source"> 
Beauchamp, Das, Pande.  Inferring Structural Ensembles from Noisy Experiments: Application to Trialanine.  In Prep.
</footer>
---
title: Biasing and Reweighting

- Project onto basis of predicted experimental observables
- Reweight using a linear free energy: $-\sum_i \alpha_i f_i(x_j)$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/model_hist0.png />
</center>

---
title: Biasing and Reweighting

- Project onto basis of predicted experimental observables
- Reweight using a linear free energy: $-\sum_i \alpha_i f_i(x_j)$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/model_hist1.png />
</center>

---
title: Biasing and Reweighting

- Project onto basis of predicted experimental observables
- Reweight using a linear free energy: $-\sum_i \alpha_i f_i(x_j)$
- $\alpha_i$ tells how populations are perturbed by $i$th experiment


<center>
<img height=300 src=figures/model_hist-1.png />
</center>

---
title: A Bayesian Framework

<center>

Assume independent normal errors. 

$\underbrace{\log P(\alpha| F_1, ..., F_n)}_{Posterior}$ = $\underbrace{-\sum_i \frac{1}{2}\frac{(\langle f_i(x)\rangle_α - F_i)^2}{\sigma_i^2}} _ {Likelihood (\chi^2)} + \underbrace{\log P(\alpha)} _ {Prior}$

Determine $\alpha$ by sampling the posterior.

</center>

<footer class="source"> 
Beauchamp, Das, Pande.  Inferring Structural Ensembles from Noisy Experiments: Application to Trialanine.  In Prep.
</footer>
---
title: FitEnsemble
subtitle: An Open-Source Python Library for Ensemble Modeling

<article>
<iframe data-src="http://nbviewer.ipython.org/urls/raw.github.com/kyleabeauchamp/FitEnsemble/master/tutorial/Tutorial1.ipynb"></iframe>
</article>

---
title: Trialanine

- Model for secondary structure / disorder peptides
- NMR Data: chemical shifts and scalar couplings

<center>
<img height=500 src=figures/ALA3.png />
</center>


<footer class="source"> Schwalbe, 2007  </footer>

---
title: Idea: Use chemical shifts and scalar couplings to reweight simulations of trialanine performed in five different force fields.

---
title: BELT Corrects Force Field Error

<center>
<img height=500 src=figures/ALA3_chi2_train.png />
</center>

---
title: Robust to Over-Fitting

<center>
<img height=500 src=figures/ALA3_chi2_test.png />
</center>

---
title: Correcting $\beta$ Bias in Amber96

<center>
<img height=500 src=figures/ALA3_rama_amber96_raw.png />
</center>

---
title: Correcting $\beta$ Bias in Amber96

<center>
<img height=500 src=figures/ALA3_rama_amber96_belt.png />
</center>

---
title: Forcefield-Independent Simulations

<center>
<img height=500 src=figures/state_0_by_forcefield.png />
</center>

---
title: Bovine Pancreatic Trypsin Inhibitor

- Workhorse in protein folding, crystallography, and NMR

<center>
<img height=500 src=figures/bpti_native.png />
</center>

<footer class="source"> 
Hope et al. Acta. Cryst., 1996. 
</footer> 

---
title: Bovine Pancreatic Trypsin Inhibitor

- Multiple disulfide (C14-C38) conformations in trypsin binding loop.

<center>
<img height=400 src=figures/C14_C38.png />
</center>

<footer class="source"> 
Palmer et al. JACS, 2003.
</footer> 

---
title: Are BPTI Simulations Consistent with Experiment?

<center>
<img height=450 src=figures/BPTI_RMSD_Shaw.png />
</center>

<footer class="source"> Shaw, 2010  </footer>

---
title: Simulation Favors Non-Native State

<center>
<img height=500 src=figures/bpti_chi14_raw.png />
</center>

<footer class="source"> 

Crystal Structure shown as X

<br>
Beauchamp, Cochran, Pande, Das.  In Prep.

</footer>

---
title: Idea: Use chemical shifts to reweight BPTI simulation.

---

title: BELT model Favors Native State

<center>
<img height=500 src=figures/bpti_chi14_belt.png />
</center>


<footer class="source"> 

Crystal Structure shown as X

<br>
Beauchamp, Cochran, Pande, Das.  In Prep.

</footer>

---
title: Models for BPTI

<center>
<img height=320 src=figures/bpti_xray.png />  <img height=320 src=figures/bpti_raw.png />  <img height=320 src=figures/bpti_belt.png />
</center>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; X-Ray &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MD &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  BELT

---
title: Falsifying BPTI Models with J Couplings

<center>
<img height=320 src=figures/bpti_xray_crossthrough.png />  <img height=320 src=figures/bpti_raw_crossthrough.png />  <img height=320 src=figures/bpti_belt.png />
</center>

&nbsp;&nbsp;&nbsp;&nbsp; $\frac{1}{n}\chi^2 = 15.0$  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  $\frac{1}{n}\chi^2 = 13.7$  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $\frac{1}{n}\chi^2 = 10.4$

<footer class="source"> Balasubramanian, 1994
</footer>

---
title: Conclusions and Future Work (BELT)

- BELT corrects forcefield bias in trialanine and BPTI
- Measure <b>all</b> scalar couplings for BPTI
- Better predictors of experimental observables: chemical shifts, scalar couplings, (TTET)

---
title: Conclusion

- MSMs parallelize MD simulation, bringing millisecond-scale dynamics within reach
- Coupling MSMs to phenomenological model of TTET allows quantitative prediction of kinetic experiments
- BELT enables experiment-driven modeling of structure and equilibrium
- Open-Source Tools for protein inference (MSMBuilder, FitEnsemble)

---
title: Acknowledgements

<center>

Rhiju and Vijay

</center>

<img height=325 src=https://lh5.googleusercontent.com/-1yMjSz9dHPA/T9pe6l08uaI/AAAAAAAAAAk/O55Qldc6QYY/s1024/image-01.jpeg />
<img height=325 src=personal_pictures/pandelab.jpg />


---
title: Acknowledgements
subtitle: Pande Lab

<font size="5">

 Greg Bowman 

 Vince Voelz

 Robert McGibbon

 Christian Schwantes

 TJ Lane

 Imran Haque
 
 Everyone!
 
</font>

---
title: Acknowledgements
subtitle: Das Lab

- Pablo Cordero
- Frank Cochran
- Fang-Chieh Chou
- Parin Sripakdeevong
- Everyone!

---

title: Acknowledgements
subtitle: Biochemistry / Biophysics

Buzz Baldwin

Dan Herschlag

Pehr Harbury

Xuesong Shi

Laura Wang, Jessica Metzger, Aimee Garza, Crystal Spitale and all the Biochem staff

Kathleen Guan

Everyone!

---
title: Acknowledgements
subtitle: Committee 

Todd Martinez

Pehr

Russ Altman

---
title: Acknowledgements

Folding@Home Donors and Forum Volunteers (Bruce Borden)

OpenMM Team: Joy Ku, Peter Eastman, Mark Friedrichs, Yutong Zhao

Thomas Kiefhaber, John Chodera, Frank Noe, Jesus Izaguirre

DE Shaw Research

Susan Marqusee, Laura Rosen

---
title: Personal Acknowledgements

<img height=250 src="https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-prn1/150375_1638963646521_6696492_n.jpg" />
<img height=250 src="https://sphotos-b.xx.fbcdn.net/hphotos-ash3/486863_437987026246966_1599482437_n.jpg" />
<img height=250 src="https://sphotos-b.xx.fbcdn.net/hphotos-frc3/737674_10100468804653513_106553532_o.jpg" />
<img height=250 src="https://sphotos-a.xx.fbcdn.net/hphotos-prn1/24510_634596556298_7990982_n.jpg" />
<img height=250 src="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash4/2661_525035797127_1171389_n.jpg" />

---
title: Thanks!
class: segue dark nobackground



---
title: A Model for TTET

<center>
<img height=500 src=figures/hp35-spheres.png />
</center>

---
title: A Model for TTET

<center>
<img height=400 src=figures/ConformationalMSM.png /> <img height=420 src=figures/ElectronicMSM-full.png />
</center>

---
title: A Model for TTET

$$P(i\rightarrow j, dark \rightarrow dark) = P_0(i\rightarrow j)$$
$$P(i\rightarrow j, dark \rightarrow light) = P_0(i\rightarrow j)$$
$$P(i\rightarrow j, light \rightarrow light) = (1 - f_i) P_0(i\rightarrow j)$$
$$P(i\rightarrow j, light \rightarrow dark) = \delta_{ij} f_i$$

---
