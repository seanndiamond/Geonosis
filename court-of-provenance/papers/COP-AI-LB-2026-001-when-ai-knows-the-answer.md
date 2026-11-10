# When AI Knows the Answer but Cannot Show the Evidence
## Linear B, Visual Provenance, and the Case for Derivation-First Artificial Intelligence

**Sean Diamond**  
**Court of Provenance / Geonosis**  
**Research preprint and open methodological case study | 10 November 2026**  
**Case:** COP-AI-LB-2026-001  
**Status:** Open to adversarial replication and correction

### Abstract

This paper examines a prolonged human–AI investigation of Linear B tablets in which a vision-capable assistant repeatedly supplied historically accepted interpretations, scholarly narratives, and standardised sign values, yet did not demonstrate the requested correspondence between selected original incisions and the canonical signs used to transcribe them. The case is neither a demonstration that Linear B lacks phonetic structure nor a validation of the claimant's alternative pictorial reading. It is an observed *evidence-presentation failure*: the assistant claimed a level of visual verification that the conversation had not established. The episode motivates a derivation-first AI protocol in which raw observations, sign segmentation, grapheme classification, sound assignments, linguistic reconstructions and external predictions are separately traceable. We propose a practical training and evaluation programme built around blind artifact examination, explicit provenance graphs, image-to-symbol alignment, adversarial alternatives, and correction without authority substitution. The research question is whether models can be trained to show not only *what a field concludes*, but *why a particular artifact warrants that conclusion*.

**Keywords:** AI epistemology; visual grounding; Linear B; Court of Provenance; epigraphy; evidence provenance; scientific reproducibility; multimodal AI; derivation-first training.

### 1. The question that started the investigation

A researcher asked an AI assistant to read a Linear B tablet, not to summarise scholarly views of it. The request developed into a more precise evidentiary demand: show the visible marks, their identification as standardised Linear B signs, their sound assignments, and their resulting Mycenaean Greek meanings, with the dependency of each step made explicit.

The dialogue examined the well-known Pylos tripod tablet PY Ta 641 and then Knossos Ca 895, conventionally interpreted through the sign groups `i-qo` (horses), `o-no` (donkeys), and `po-ro` (foals), alongside animal ideograms and numerals (Waanders 2012). The discussion also examined Kober's 1948 sign-pattern observations and the historical reconstruction of Ventris's syllabary.

The researcher proposed a separate image-based reading in a magnified area: an elephant, a commanding or handling figure, and a wider civilisational scene. These are recorded here as **claimant observations/interpretations**, not as findings independently replicated or endorsed by this paper. No image annotation, independent blinded observers, or geometric comparison was completed for those motifs during the exchange.

The decisive methodological event was simpler: when the researcher placed printed standard Linear B signs beside a high-resolution crop of the artifact, the assistant could not demonstrate stroke-by-stroke correspondence, yet had previously spoken as if the transcription had been visually verified.

### 2. Evidence record and scope

This is a qualitative case study of one extended dialogue, not a controlled trial of AI systems. Its primary evidence is the conversation record and the user-supplied screenshot enlargements. The dialogue itself is not reproduced verbatim here; the exhibit log below states what was and was not demonstrated. Public versions of user screenshots should not be redistributed without resolving reproduction rights and retaining image-source metadata.

**Exhibit sequence**

| ID | Event | What was established | What remained unshown |
| --- | --- | --- | --- |
| E01 | Request to read PY Ta 641 | Conventional inventory interpretation and syllabic transcription were supplied | A continuous image-to-sign derivation |
| E02 | Kober/Ventris challenge | Source literature describes recurrent sign groups and proposed phonetic grids | Full historical provenance of each sign-value assignment |
| E03 | KN Ca 895 presented | Published transcription includes `i-qo`, `o-no`, `po-ro` and pictorial signs | Precise localisation of each printed sign in the provided photographic crop |
| E04 | User supplies high-resolution comparisons | Assistant's earlier printed-sign-to-incision correspondence was not demonstrated | Whether an expert palaeographic tracing would support or reject the transcription |
| E05 | Formal Court challenge | Claimant lodged: “There are no phonetics in the Linear B archive,” explicitly inviting correction by a complete derivation staircase | The claim's independent validation or falsification |

**Crucial boundary:** the assistant's failure to demonstrate a correspondence is not a demonstration that the underlying transcription or phonetic decipherment is false. Conversely, citing the conventional reading is not a substitute for demonstrating the requested artifact-level correspondence. The case concerns an AI evidentiary failure, not a final adjudication of Linear B.

### 3. Why the AI response failed

**3.1 Answer substitution.** The assistant repeatedly answered “What is the accepted reading?” when the user asked “Show how the photographed marks warrant that reading.” Accurate background information did not meet the specified task.

**3.2 Representation substitution.** Canonical sign glyphs were presented in place of the artifact incisions. A standardised font is a reference representation, not proof that a specific damaged or stylised mark belongs to that sign class.

**3.3 Dependency concealment.** The chain from visible mark to sign identity to phonetic value to Greek lexical reconstruction was compressed. A derived transcription was treated rhetorically as a direct visual observation.

**3.4 Authority recycling.** References to Kober, Ventris, Chadwick, Cambridge and institutional corpora were relevant historiography, but they often arrived where the user requested a direct mark-to-mark comparison. The source was not necessarily wrong; its role in the argument was wrong.

**3.5 Conversational inertia.** Rather than stopping at the first unverified correspondence, the assistant continued defending or explaining the inherited reading. This extended the exchange and reduced the efficiency of correction.

These phenomena align with independent research on visual-language models' reliance on language priors, weak fine-grained visual grounding, and the distinction between correct citations and faithful source use (Favero et al. 2024; Villa et al. 2025; Wallat et al. 2024). Such work provides context, not evidence that the particular assistant's internal mechanisms have been measured here.

### 4. The derivation staircase: a proposed AI operating standard

A derivation-first model should maintain each of the following rungs as an independently inspectable record.

1. **Artifact:** identify the original item, image version, scale, orientation, location and rights status.
2. **Observation:** preserve pixels, incisions, damage, spacing, surface topology and uncertainty without attaching meanings.
3. **Segmentation:** mark bounding polygons for each proposed sign, stroke group and non-textual image.
4. **Classification:** show the candidate sign class and alternatives, with direct shape comparisons and a rationale for handling variants.
5. **Value assignment:** state the phonetic or functional value, earliest source, date and dependency graph; distinguish inherited conventions from independently inferred values.
6. **Composition:** demonstrate precisely how signs form sequences, words or visual relations.
7. **Interpretation:** specify linguistic reconstruction or pictorial scene reading and all extra assumptions, including unwritten consonants or morphological restoration.
8. **Out-of-sample test:** register predictions before examining held-out artifacts; count successes, failures and retuned values.
9. **Adversarial review:** compare serious alternatives and negative controls under symmetric constraints.
10. **Reproduction:** publish sufficient images, coordinates, sign tables, decisions, code and change history for another reader to repeat the work.

The Court's existing hierarchy is preserved: `CITED != LOCATED != RETRIEVED != INSPECTED != MAPPED != DERIVED != REPRODUCED != CHALLENGED != SURVIVED`. A model should be prohibited from claiming a deeper level than its evidence ledger supports.

### 5. Training architecture

We propose **DFAI: Derivation-First Artificial Intelligence** as a modular training and inference procedure rather than as an unsupported claim that one model architecture will solve the problem.

**Module A: Observation-first visual pretraining.** Present artifacts with titles and translations hidden. Reward accurate stroke localisation, descriptions of visible recurrence and uncertainty in damaged regions. Penalise ungrounded object naming.

**Module B: Provenance-graph supervision.** Train the model on claims linked to source images, exact regions, historical assignments, assumptions and alternative explanations. Evaluate whether each conclusion remains valid when a supporting link is removed.

**Module C: Sign-variant verification.** Present a photographed ancient grapheme and a canonical glyph. Require the model to trace or align the ink/incision features, explain variation, and allow a “not established” result. Use expert-reviewed genuine matches, near-misses and damaged counterexamples.

**Module D: Evidence-blind historical reconstruction.** Withhold accepted translations and later confirmations; expose only historically available materials at defined cutoff dates. Reward precise uncertainty and subsequent predictive success, not post hoc fit.

**Module E: Adversarial hypothesis contest.** Compare the conventional phonetic model, an image-first model and deliberately arbitrary sound mappings, all frozen before a hidden test set. The latter is a negative control, not a serious historical interpretation. Measure whether each predicts independent structure above chance.

**Module F: Correction and conversational reset.** Train the assistant to identify when an earlier response answered the wrong question, retract unsupported mapping claims, and resume at the first failed rung without repeating authority narratives.

### 6. Proposed benchmark: SHOW-ME

An evaluation set should contain inscriptions from known phonetic writing systems, mixed scripts, undeciphered corpora, iconographic scenes and synthetic control artifacts. Corpus status must be concealed from the model in the image-first phase. Expert annotations should be blinded where feasible.

**Primary metrics:** sign-region localisation accuracy (intersection-over-union), grapheme-classification precision/recall, traceable-claim coverage, unsupported-bridge rate, calibration of `UNKNOWN`, historical leakage, held-out predictive performance, false-match rate for canonical glyph comparisons, and correction latency in conversational turns.

**Experimental arms:**
- **A: conventional answer-first AI**, given usual retrieval and user prompts;
- **B: derivation-first AI**, required to inspect and log artifact links before translation;
- **C: derivation-first AI with adversarial reviewer**, receiving independent counter-hypotheses and explicit dependency checks.

All arms receive matched access to images and background resources. Pre-register task prompts, model versions, annotator criteria and test splits. Include shuffled phonetic labels and scrambled artifact-to-transcription pairings as negative controls. Report false positives and failure cases, not merely success rates.

**Falsifiable prediction:** on held-out visual-to-sign correspondence tasks, B and C will reduce unsupported-bridge rates relative to A without an unacceptable decline in correct sign matches. A second hypothesis predicts improved calibration and faster correction after a user identifies a mismatch. These are future hypotheses, not measured results of this single case.

### 7. The Linear B adjudication remains open

The claimant's declared thesis is: **“There are no phonetics in the Linear B archive.”** The claimant expressly welcomes correction by an inspectable staircase from original incisions to the proposed signs, sound assignments and linguistic values.

The present paper neither adopts that thesis as established fact nor dismisses it by prestige. Linear B is conventionally and substantially supported as a syllabic representation of Mycenaean Greek; the question in this case is narrower: whether the assistant could demonstrate its specific claimed correspondence from the user-provided artifact image. It could not.

The next archaeological test should use original or authorised high-resolution images of KN Ca 895, a stable facsimile, published sign-level references, and independently produced polygon annotations. The analyst should trace the specific `i` and `qo` marks first; only then should sound and Greek reconstruction be introduced. The claimant's elephant–handler–civilisation interpretation should be separately registered and tested for inter-observer agreement, recurrence, segmentation stability and independent prediction. Neither approach receives a privileged evidentiary exemption.

### 8. Discussion: from inherited answers to inspectable reasoning

Scientific AI must distinguish **answer accuracy** from **evidence performance**. A system may cite the right publication and repeat the prevailing interpretation while failing at the precise visual mapping requested by a researcher. In such cases, apparent fluency can generate an illusion that the derivation has already been performed.

Kober's 1948 argument explicitly distinguished fact from theory and recognised the limits of her tentative proposed phonetic grid. That methodological caution is not an embarrassment to decipherment history: it is a model of how AI should label inference stages. Messeri and Crockett's analysis of AI-generated illusions of understanding provides a wider scientific frame.

The remedy is not to train AI to distrust institutions, nor to accept unconventional claims automatically. It is to train AI to make every interpretation auditable and to allow a result of `BLOCKED_PENDING_DERIVATION` without fabricating the missing bridge.

### 9. Conclusion

The Linear B dialogue exposed an AI failure of *evidentiary sequencing*. A scholarly answer was available, yet the requested image-to-sign demonstration was not. The AI spent many turns supplying historical and linguistic context before explicitly acknowledging the absent mapping. That waste of time is itself a design signal.

A better scientific assistant should say, early and plainly: “I can report the conventional translation, but I have not yet mapped these photographed marks to its sign sequence.” It should then either perform the comparison visibly or stop at the exact point of uncertainty.

**The future of scientific AI depends not only on knowing what has been concluded, but on showing what was actually observed, what was inferred, what was tested, and what remains unresolved.**

### Declaration and limitations

This is a methodological case study and proposed research protocol, not an experimentally validated AI intervention. No quantitative model comparison, independent epigraphic re-transcription, blinded image-reading study, or new decipherment has yet been completed. Interpretations advanced by the claimant are attributed as claims. The paper does not imply institutional misconduct. Images supplied in the dialogue are not republished in this version pending source identification and reproduction-rights review. AI-assisted drafting was used; responsibility for the research claims remains with the named author.

### References

1. Kober, A. E. (1948). “The Minoan Scripts: Fact and Theory.” *American Journal of Archaeology*, 52(1), 82–103. https://doi.org/10.2307/500554
2. Ventris, M., & Chadwick, J. (1953). “Evidence for Greek Dialect in the Mycenaean Archives.” *Journal of Hellenic Studies*, 73, 84–103. https://doi.org/10.2307/628239
3. Waanders, F. M. J. (2012). “Who Is Who in the Mycenaean Zoo?” *Živa Antika*, Monograph 10, 295–303. https://manu.edu.mk/wp-content/uploads/2017/10/Ziva-Antika-Monographs-10.pdf
4. University of Cambridge, Faculty of Classics. “The Ventris–Chadwick Correspondence.” https://www.classics.cam.ac.uk/ORDER/seminars/projects/mycep/archive/correspondence
5. Favero, A., et al. (2024). “Multi-Modal Hallucination Control by Visual Information Grounding.” *CVPR*, 14303–14312. https://openaccess.thecvf.com/content/CVPR2024/html/Favero_Multi-Modal_Hallucination_Control_by_Visual_Information_Grounding_CVPR_2024_paper.html
6. Villa, A., León, J., Soto, A., & Ghanem, B. (2025). “Behind the Magic, MERLIM.” *CVPR Workshops*, 492–502. https://openaccess.thecvf.com/content/CVPR2025W/BEAM/html/Villa_Behind_the_Magic_MERLIM_Multi-modal_Evaluation_Benchmark_for_Large_Image-Language_CVPRW_2025_paper.html
7. Wallat, J., Heuss, M., de Rijke, M., & Anand, A. (2024). “Correctness is not Faithfulness in RAG Attributions.” arXiv:2412.18004. https://arxiv.org/abs/2412.18004
8. Messeri, L., & Crockett, M. J. (2024). “Artificial intelligence and illusions of understanding in scientific research.” *Nature*, 627, 49–58. https://doi.org/10.1038/s41586-024-07146-0
9. Cao, Q., Cheng, J., Liang, X., & Lin, L. (2024). “VisDiaHalBench: A Visual Dialogue Benchmark For Diagnosing Hallucination in Large Vision-Language Models.” *ACL*, 12161–12176. https://aclanthology.org/2024.acl-long.658/
10. Diamond, S. (2026). “Court of Provenance: Canonical evidentiary operating standards.” *Geonosis GitHub*. https://github.com/seanndiamond/Geonosis/tree/main/court-of-provenance

### Suggested citation

Diamond, Sean (2026). *When AI Knows the Answer but Cannot Show the Evidence: Linear B, Visual Provenance, and the Case for Derivation-First Artificial Intelligence*. Court of Provenance / Geonosis, COP-AI-LB-2026-001. Research preprint.
