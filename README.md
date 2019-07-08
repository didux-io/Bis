# Smilo Bis

Biometric Identity Service

```
docker-compose up -d
```

# Available endpoints

## POST /add

### Request
```
{
    "smartcontract": "0x0001234",
    "model_version": 2,
    "vector": [ 0.045072222, 0.04920785, -0.02904682, 0.03295613, -0.10173341, 0.061261676, -0.041644942, -0.011714032, -0.0007638014, 0.013426632, 0.078980684, -0.023040678, -0.023766287, -0.060508113, -0.034092505, -0.0493085, -0.06545257, -0.006726077, 0.053886272, -0.046059486, -0.07982736, -0.0462191, 0.070958346, 0.043853153, 0.007771763, 0.036524847, -0.026366174, 0.014500886, -0.07641726, 0.030485714, 0.005366321, 0.006778425, -0.0824544, 0.038469978, -0.087317765, 0.02006116, 0.01985979, 0.030208068, 0.08629569, -0.027493201, 0.08297847, -0.019376794, 0.06742019, -0.0064247507, -0.008600561, 0.03028297, 0.053982258, 0.04353566, -0.0028632842, -0.013216027, 0.0801902, -0.069956556, -0.036781203, 0.006468473, 0.059726454, -0.08318524, 0.047470745, 0.08748002, -0.011264092, 0.03749837, -0.003337898, 0.102985464, -0.007926104, 0.0005788804, 0.0027599246, -0.08073838, -0.06513127, 0.0052446765, -0.07229885, -0.010942269, 0.06239584, -0.005052562, -0.049072947, 0.051248793, 0.012361474, -0.053238306, -0.0011935255, 0.00095276965, 0.07036074, -0.03573784, 0.026461108, 0.05855167, -0.04950662, -0.016842213, -0.010621803, -0.0043328013, -0.00966704, 0.0056433654, 0.029758535, 0.028406655, 0.034857318, -0.050106462, -0.00044623172, -0.014681457, 0.056904655, -0.064189784, 0.005484812, -0.05620866, -0.08416334, 0.0363165, 0.037372887, -0.06320958, 0.028902635, -0.03314197, -0.026194183, 0.011191976, 0.02374335, 0.10213661, -0.028110769, 0.011284948, -0.0173405, 0.042138655, -0.011696288, -0.011352354, 0.0029103202, -0.030992107, 0.05003412, -0.04160747, -0.022227105, -0.024105836, -0.013605321, 0.067972355, -0.08729069, 0.016046263, -0.029374737, 0.073821135, 0.10062143, 0.0037642845, 0.04695158, 0.026456552, 0.0057056732, -0.015090563, 0.018549792, 0.010473753, 0.05341478, 0.013405586, 0.028016565, 0.054269057, 0.08261276, 0.0640826, 0.031868257, 0.041529134, -0.1193124, 0.02575855, 0.002218912, 0.013953121, -0.045781415, 0.016661908, -0.03730826, 0.0012722211, 0.01101277, 0.039991807, -0.08105098, 0.042300057, -0.032462444, -0.07553389, 0.039561637, -0.0030918338, -0.02314517, 0.039516184, -0.065739706, 0.013644432, -0.037832864, 0.01774884, -0.015173196, 0.0077528763, 0.027736446, -0.024380315, 0.013510356, -0.049578745, 0.054739233, -0.028905049, -0.06311056, 0.008303631, 0.0130252885, -0.10731462, -0.0071302475, -0.042548295, 0.06924551, -0.0358428, -0.07182659, 0.07362726, -0.000971949, 0.0047599934, 0.08609071, 0.005453628, -0.023502856, -0.0068391953, 0.050189953, 0.021354178, -0.03956673, 0.011735134, 0.052449394, 0.044525303, 0.021317434, 0.014866376, 0.044837147, -0.020781435, 0.0025789225, -0.019803768, -0.040273543, -0.017665222, 0.038699374, -0.045248285, -0.011829716, -0.028008549, -0.018192401, 0.033273578, 0.02818122, 0.07883436, 0.011172835, 0.09928881, -0.024641158, 0.07377902, -0.052364334, -0.0070692385, -0.0056475797, 0.004419087, 0.057591785, 0.021634525, -0.031315498, 0.015763637, -0.031909324, -0.016252346, 0.037897125, 0.062578715, -0.018052153, 0.009488923, -0.0118210865, 0.048998732, -0.0370828, -0.043561943, 0.07207013, 0.0077333953, 0.0053092274, -0.1176542, 0.018551247, -0.038774487, -0.00927329, 0.012295564, 0.060879994, -0.04267501, 0.0092065465, -0.065611534, -0.0016155123, 0.06485345, -0.06595335, -0.0016172811, 0.007243553, 0.07787549, 0.039496128, -0.010579236, 0.038417462, -0.057369087, -0.014830442, 0.018113509, -0.0042045293, -0.003735559, 0.045082003, -0.014470849, -0.012470777, 0.05472394, 0.0134279225, -0.08291089, -0.05197683, -0.03482191, -0.07442592, 0.028989498, 0.07063685, -0.030866722, -0.054311145, 0.06723736, 0.035231706, 0.048609745, -0.017898891, 0.024527993, 0.005743421, 0.04557067, 0.028730752, 0.010791047, -0.02234316, -0.05896296, -0.006848022, 0.019544417, 0.001226287, 0.032368217, -0.026513696, 0.027487036, 0.10057621, -0.031203408, -0.0869804, -0.06815365, -0.011945394, -0.031250782, -0.0048992676, -0.002277884, -0.009324404, 0.075424016, 0.03264504, -0.07450931, 0.05406487, 0.028881747, 0.022332178, 0.040338308, 0.018308025, 0.019354092, -0.012393984, 0.01676731, 0.027108377, 0.05567101, 0.014940892, 0.029818071, -0.034134753, -0.01688087, 0.12879194, -0.019805666, -0.10493562, 0.049413655, 0.052358598, -0.05075315, -0.06072704, -0.04525789, -0.046887178, 0.06197186, -0.038741402, 0.031881686, -0.04450079, 0.057923626, -0.037183028, 0.0075087184, -0.042485263, 0.014395331, -0.0754588, 0.032288637, 0.03739583, 0.029219033, -0.033374228, -0.024631916, -0.001991407, -0.038220547, 0.008985744, -0.019850299, -0.052556653, 0.06874115, -0.02901948, 0.002024821, -0.014353842, -0.021093452, 0.049113836, 0.06234979, 0.09749797, -0.056544013, -0.02171563, -0.04201525, -0.08762511, -0.004446675, 0.07023024, 0.031241722, 0.057314176, 0.02530817, 0.022190697, 0.06847545, 0.03461445, 0.026020546, -0.10987655, 0.05989899, 0.09781558, 0.01547654, -0.010726338, 0.058997896, 0.005457997, 0.020382224, 0.032869726, -0.007028506, 0.053979795, 0.037023723, 0.013422062, -0.0072336257, 0.019828092, 0.006555522, -0.056179103, -0.047110956, 0.032058395, -0.018442823, -0.055354975, -0.029859532, -0.007579957, 0.0143733, 0.05182567, -0.0005421792, -0.08507183, 0.04911044, 0.017550083, 0.0015048551, -0.0029476276, 0.07057404, -0.03733388, 0.0018684345, 0.06166133, -0.011150358, -0.0077351555, -0.028162204, -0.11196239, -0.09236244, 0.055049483, 0.05579075, -0.005223511, -0.0435036, -0.04896749, -0.03345477, 0.0038895514, 0.017122723, -0.07208417, 0.016996462, 0.0065576, 0.025109183, 0.01175039, 0.03366881, 0.07141689, -0.014054037, 0.016879817, 0.031477056, 0.03632796, 0.06395024, -0.04220069, 0.0062176483, -0.022527335, -0.025984455, -0.0647694, 0.054601815, -0.015159034, 0.014657266, 0.04409256, -0.015946683, 0.011887132, 0.026414476, 0.020927155, -0.016512435, 0.09359048, 0.029739358, -0.066180184, 0.082244694, 0.0007292507, -0.06282271, 0.035395358, -0.100961864, 0.014836456, 0.11625059, -0.023679407, -0.013240734, 0.019296095, -0.028371686, 0.016569745, 0.008198354, -0.002588122, -0.061931096, -0.019892568, -0.011799377, 0.016310172, -0.0044856467, -0.0267413, -0.005191055, 0.04924748, -0.0053692097, -0.03609329, 0.049340405, 0.011295922, 0.069036305, 0.0036290872, -0.0040835966, 0.0035751562, -0.035198208, -0.0015323451, 0.030191373, 0.0015703973, -0.018142749, -0.011257919, -0.00057657144, -0.053825088, 0.01760392, -0.001581838, 0.02007053, -0.05818865, 0.04108587, -0.028711911, 0.03198221, 0.005932087, -0.01670024, 0.0047082426, 0.025187634, -0.0069206334, -0.020081813, 0.0058442047, -0.0054093692, -0.07816217, -0.04283457, 0.05345854, -0.018779771, 0.056370307, 0.057341665, -0.012000827, -0.032532148, 0.01690849, 0.06947271, -0.017020883, 0.014368475, -0.07444708, -0.013201608, -0.003327813, -0.0357886, -0.014834576, -0.011255137 ]
}
```

### Response
```
[]
```
Status 200

## GET /get/\<smartcontract>

Returns biometrics for \<smartcontract>

### Response
```
{
    "model_version": 2,
    "smartcontract": "0x0001234",
    "vector": "(0.045072222, 0.04920785, -0.02904682, 0.03295613, -0.10173341, 0.061261676, -0.041644942, -0.011714032, -0.0007638014, 0.013426632, 0.078980684, -0.023040678, -0.023766287, -0.060508113, -0.034092505, -0.0493085, -0.06545257, -0.006726077, 0.053886272, -0.046059486, -0.07982736, -0.0462191, 0.070958346, 0.043853153, 0.007771763, 0.036524847, -0.026366174, 0.014500886, -0.07641726, 0.030485714, 0.005366321, 0.006778425, -0.0824544, 0.038469978, -0.087317765, 0.02006116, 0.01985979, 0.030208068, 0.08629569, -0.027493201, 0.08297847, -0.019376794, 0.06742019, -0.0064247507, -0.008600561, 0.03028297, 0.053982258, 0.04353566, -0.0028632842, -0.013216027, 0.0801902, -0.069956556, -0.036781203, 0.006468473, 0.059726454, -0.08318524, 0.047470745, 0.08748002, -0.011264092, 0.03749837, -0.003337898, 0.102985464, -0.007926104, 0.0005788804, 0.0027599246, -0.08073838, -0.06513127, 0.0052446765, -0.07229885, -0.010942269, 0.06239584, -0.005052562, -0.049072947, 0.051248793, 0.012361474, -0.053238306, -0.0011935255, 0.00095276965, 0.07036074, -0.03573784, 0.026461108, 0.05855167, -0.04950662, -0.016842213, -0.010621803, -0.0043328013, -0.00966704, 0.0056433654, 0.029758535, 0.028406655, 0.034857318, -0.050106462, -0.00044623172, -0.014681457, 0.056904655, -0.064189784, 0.005484812, -0.05620866, -0.08416334, 0.0363165, 0.037372887, -0.06320958, 0.028902635, -0.03314197, -0.026194183, 0.011191976, 0.02374335, 0.10213661, -0.028110769, 0.011284948, -0.0173405, 0.042138655, -0.011696288, -0.011352354, 0.0029103202, -0.030992107, 0.05003412, -0.04160747, -0.022227105, -0.024105836, -0.013605321, 0.067972355, -0.08729069, 0.016046263, -0.029374737, 0.073821135, 0.10062143, 0.0037642845, 0.04695158, 0.026456552, 0.0057056732, -0.015090563, 0.018549792, 0.010473753, 0.05341478, 0.013405586, 0.028016565, 0.054269057, 0.08261276, 0.0640826, 0.031868257, 0.041529134, -0.1193124, 0.02575855, 0.002218912, 0.013953121, -0.045781415, 0.016661908, -0.03730826, 0.0012722211, 0.01101277, 0.039991807, -0.08105098, 0.042300057, -0.032462444, -0.07553389, 0.039561637, -0.0030918338, -0.02314517, 0.039516184, -0.065739706, 0.013644432, -0.037832864, 0.01774884, -0.015173196, 0.0077528763, 0.027736446, -0.024380315, 0.013510356, -0.049578745, 0.054739233, -0.028905049, -0.06311056, 0.008303631, 0.0130252885, -0.10731462, -0.0071302475, -0.042548295, 0.06924551, -0.0358428, -0.07182659, 0.07362726, -0.000971949, 0.0047599934, 0.08609071, 0.005453628, -0.023502856, -0.0068391953, 0.050189953, 0.021354178, -0.03956673, 0.011735134, 0.052449394, 0.044525303, 0.021317434, 0.014866376, 0.044837147, -0.020781435, 0.0025789225, -0.019803768, -0.040273543, -0.017665222, 0.038699374, -0.045248285, -0.011829716, -0.028008549, -0.018192401, 0.033273578, 0.02818122, 0.07883436, 0.011172835, 0.09928881, -0.024641158, 0.07377902, -0.052364334, -0.0070692385, -0.0056475797, 0.004419087, 0.057591785, 0.021634525, -0.031315498, 0.015763637, -0.031909324, -0.016252346, 0.037897125, 0.062578715, -0.018052153, 0.009488923, -0.0118210865, 0.048998732, -0.0370828, -0.043561943, 0.07207013, 0.0077333953, 0.0053092274, -0.1176542, 0.018551247, -0.038774487, -0.00927329, 0.012295564, 0.060879994, -0.04267501, 0.0092065465, -0.065611534, -0.0016155123, 0.06485345, -0.06595335, -0.0016172811, 0.007243553, 0.07787549, 0.039496128, -0.010579236, 0.038417462, -0.057369087, -0.014830442, 0.018113509, -0.0042045293, -0.003735559, 0.045082003, -0.014470849, -0.012470777, 0.05472394, 0.0134279225, -0.08291089, -0.05197683, -0.03482191, -0.07442592, 0.028989498, 0.07063685, -0.030866722, -0.054311145, 0.06723736, 0.035231706, 0.048609745, -0.017898891, 0.024527993, 0.005743421, 0.04557067, 0.028730752, 0.010791047, -0.02234316, -0.05896296, -0.006848022, 0.019544417, 0.001226287, 0.032368217, -0.026513696, 0.027487036, 0.10057621, -0.031203408, -0.0869804, -0.06815365, -0.011945394, -0.031250782, -0.0048992676, -0.002277884, -0.009324404, 0.075424016, 0.03264504, -0.07450931, 0.05406487, 0.028881747, 0.022332178, 0.040338308, 0.018308025, 0.019354092, -0.012393984, 0.01676731, 0.027108377, 0.05567101, 0.014940892, 0.029818071, -0.034134753, -0.01688087, 0.12879194, -0.019805666, -0.10493562, 0.049413655, 0.052358598, -0.05075315, -0.06072704, -0.04525789, -0.046887178, 0.06197186, -0.038741402, 0.031881686, -0.04450079, 0.057923626, -0.037183028, 0.0075087184, -0.042485263, 0.014395331, -0.0754588, 0.032288637, 0.03739583, 0.029219033, -0.033374228, -0.024631916, -0.001991407, -0.038220547, 0.008985744, -0.019850299, -0.052556653, 0.06874115, -0.02901948, 0.002024821, -0.014353842, -0.021093452, 0.049113836, 0.06234979, 0.09749797, -0.056544013, -0.02171563, -0.04201525, -0.08762511, -0.004446675, 0.07023024, 0.031241722, 0.057314176, 0.02530817, 0.022190697, 0.06847545, 0.03461445, 0.026020546, -0.10987655, 0.05989899, 0.09781558, 0.01547654, -0.010726338, 0.058997896, 0.005457997, 0.020382224, 0.032869726, -0.007028506, 0.053979795, 0.037023723, 0.013422062, -0.0072336257, 0.019828092, 0.006555522, -0.056179103, -0.047110956, 0.032058395, -0.018442823, -0.055354975, -0.029859532, -0.007579957, 0.0143733, 0.05182567, -0.0005421792, -0.08507183, 0.04911044, 0.017550083, 0.0015048551, -0.0029476276, 0.07057404, -0.03733388, 0.0018684345, 0.06166133, -0.011150358, -0.0077351555, -0.028162204, -0.11196239, -0.09236244, 0.055049483, 0.05579075, -0.005223511, -0.0435036, -0.04896749, -0.03345477, 0.0038895514, 0.017122723, -0.07208417, 0.016996462, 0.0065576, 0.025109183, 0.01175039, 0.03366881, 0.07141689, -0.014054037, 0.016879817, 0.031477056, 0.03632796, 0.06395024, -0.04220069, 0.0062176483, -0.022527335, -0.025984455, -0.0647694, 0.054601815, -0.015159034, 0.014657266, 0.04409256, -0.015946683, 0.011887132, 0.026414476, 0.020927155, -0.016512435, 0.09359048, 0.029739358, -0.066180184, 0.082244694, 0.0007292507, -0.06282271, 0.035395358, -0.100961864, 0.014836456, 0.11625059, -0.023679407, -0.013240734, 0.019296095, -0.028371686, 0.016569745, 0.008198354, -0.002588122, -0.061931096, -0.019892568, -0.011799377, 0.016310172, -0.0044856467, -0.0267413, -0.005191055, 0.04924748, -0.0053692097, -0.03609329, 0.049340405, 0.011295922, 0.069036305, 0.0036290872, -0.0040835966, 0.0035751562, -0.035198208, -0.0015323451, 0.030191373, 0.0015703973, -0.018142749, -0.011257919, -0.00057657144, -0.053825088, 0.01760392, -0.001581838, 0.02007053, -0.05818865, 0.04108587, -0.028711911, 0.03198221, 0.005932087, -0.01670024, 0.0047082426, 0.025187634, -0.0069206334, -0.020081813, 0.0058442047, -0.0054093692, -0.07816217, -0.04283457, 0.05345854, -0.018779771, 0.056370307, 0.057341665, -0.012000827, -0.032532148, 0.01690849, 0.06947271, -0.017020883, 0.014368475, -0.07444708, -0.013201608, -0.003327813, -0.0357886, -0.014834576, -0.011255137)"
}
```
Status 200

## POST /search

### Request
```
{
    "vector": [ 0.045072222, 0.05920785, -0.12904682, 0.03295613, -0.10173341, 0.061261676, -0.041644942, -0.011714032, -0.0007638014, 0.013426632, 0.078980684, -0.023040678, -0.023766287, -0.060508113, -0.034092505, -0.0493085, -0.06545257, -0.006726077, 0.053886272, -0.046059486, -0.07982736, -0.0462191, 0.070958346, 0.043853153, 0.007771763, 0.036524847, -0.026366174, 0.014500886, -0.07641726, 0.030485714, 0.005366321, 0.006778425, -0.0824544, 0.038469978, -0.087317765, 0.02006116, 0.01985979, 0.030208068, 0.08629569, -0.027493201, 0.08297847, -0.019376794, 0.06742019, -0.0064247507, -0.008600561, 0.03028297, 0.053982258, 0.04353566, -0.0028632842, -0.013216027, 0.0801902, -0.069956556, -0.036781203, 0.006468473, 0.059726454, -0.08318524, 0.047470745, 0.08748002, -0.011264092, 0.03749837, -0.003337898, 0.102985464, -0.007926104, 0.0005788804, 0.0027599246, -0.08073838, -0.06513127, 0.0052446765, -0.07229885, -0.010942269, 0.06239584, -0.005052562, -0.049072947, 0.051248793, 0.012361474, -0.053238306, -0.0011935255, 0.00095276965, 0.07036074, -0.03573784, 0.026461108, 0.05855167, -0.04950662, -0.016842213, -0.010621803, -0.0043328013, -0.00966704, 0.0056433654, 0.029758535, 0.028406655, 0.034857318, -0.050106462, -0.00044623172, -0.014681457, 0.056904655, -0.064189784, 0.005484812, -0.05620866, -0.08416334, 0.0363165, 0.037372887, -0.06320958, 0.028902635, -0.03314197, -0.026194183, 0.011191976, 0.02374335, 0.10213661, -0.028110769, 0.011284948, -0.0173405, 0.042138655, -0.011696288, -0.011352354, 0.0029103202, -0.030992107, 0.05003412, -0.04160747, -0.022227105, -0.024105836, -0.013605321, 0.067972355, -0.08729069, 0.016046263, -0.029374737, 0.073821135, 0.10062143, 0.0037642845, 0.04695158, 0.026456552, 0.0057056732, -0.015090563, 0.018549792, 0.010473753, 0.05341478, 0.013405586, 0.028016565, 0.054269057, 0.08261276, 0.0640826, 0.031868257, 0.041529134, -0.1193124, 0.02575855, 0.002218912, 0.013953121, -0.045781415, 0.016661908, -0.03730826, 0.0012722211, 0.01101277, 0.039991807, -0.08105098, 0.042300057, -0.032462444, -0.07553389, 0.039561637, -0.0030918338, -0.02314517, 0.039516184, -0.065739706, 0.013644432, -0.037832864, 0.01774884, -0.015173196, 0.0077528763, 0.027736446, -0.024380315, 0.013510356, -0.049578745, 0.054739233, -0.028905049, -0.06311056, 0.008303631, 0.0130252885, -0.10731462, -0.0071302475, -0.042548295, 0.06924551, -0.0358428, -0.07182659, 0.07362726, -0.000971949, 0.0047599934, 0.08609071, 0.005453628, -0.023502856, -0.0068391953, 0.050189953, 0.021354178, -0.03956673, 0.011735134, 0.052449394, 0.044525303, 0.021317434, 0.014866376, 0.044837147, -0.020781435, 0.0025789225, -0.019803768, -0.040273543, -0.017665222, 0.038699374, -0.045248285, -0.011829716, -0.028008549, -0.018192401, 0.033273578, 0.02818122, 0.07883436, 0.011172835, 0.09928881, -0.024641158, 0.07377902, -0.052364334, -0.0070692385, -0.0056475797, 0.004419087, 0.057591785, 0.021634525, -0.031315498, 0.015763637, -0.031909324, -0.016252346, 0.037897125, 0.062578715, -0.018052153, 0.009488923, -0.0118210865, 0.048998732, -0.0370828, -0.043561943, 0.07207013, 0.0077333953, 0.0053092274, -0.1176542, 0.018551247, -0.038774487, -0.00927329, 0.012295564, 0.060879994, -0.04267501, 0.0092065465, -0.065611534, -0.0016155123, 0.06485345, -0.06595335, -0.0016172811, 0.007243553, 0.07787549, 0.039496128, -0.010579236, 0.038417462, -0.057369087, -0.014830442, 0.018113509, -0.0042045293, -0.003735559, 0.045082003, -0.014470849, -0.012470777, 0.05472394, 0.0134279225, -0.08291089, -0.05197683, -0.03482191, -0.07442592, 0.028989498, 0.07063685, -0.030866722, -0.054311145, 0.06723736, 0.035231706, 0.048609745, -0.017898891, 0.024527993, 0.005743421, 0.04557067, 0.028730752, 0.010791047, -0.02234316, -0.05896296, -0.006848022, 0.019544417, 0.001226287, 0.032368217, -0.026513696, 0.027487036, 0.10057621, -0.031203408, -0.0869804, -0.06815365, -0.011945394, -0.031250782, -0.0048992676, -0.002277884, -0.009324404, 0.075424016, 0.03264504, -0.07450931, 0.05406487, 0.028881747, 0.022332178, 0.040338308, 0.018308025, 0.019354092, -0.012393984, 0.01676731, 0.027108377, 0.05567101, 0.014940892, 0.029818071, -0.034134753, -0.01688087, 0.12879194, -0.019805666, -0.10493562, 0.049413655, 0.052358598, -0.05075315, -0.06072704, -0.04525789, -0.046887178, 0.06197186, -0.038741402, 0.031881686, -0.04450079, 0.057923626, -0.037183028, 0.0075087184, -0.042485263, 0.014395331, -0.0754588, 0.032288637, 0.03739583, 0.029219033, -0.033374228, -0.024631916, -0.001991407, -0.038220547, 0.008985744, -0.019850299, -0.052556653, 0.06874115, -0.02901948, 0.002024821, -0.014353842, -0.021093452, 0.049113836, 0.06234979, 0.09749797, -0.056544013, -0.02171563, -0.04201525, -0.08762511, -0.004446675, 0.07023024, 0.031241722, 0.057314176, 0.02530817, 0.022190697, 0.06847545, 0.03461445, 0.026020546, -0.10987655, 0.05989899, 0.09781558, 0.01547654, -0.010726338, 0.058997896, 0.005457997, 0.020382224, 0.032869726, -0.007028506, 0.053979795, 0.037023723, 0.013422062, -0.0072336257, 0.019828092, 0.006555522, -0.056179103, -0.047110956, 0.032058395, -0.018442823, -0.055354975, -0.029859532, -0.007579957, 0.0143733, 0.05182567, -0.0005421792, -0.08507183, 0.04911044, 0.017550083, 0.0015048551, -0.0029476276, 0.07057404, -0.03733388, 0.0018684345, 0.06166133, -0.011150358, -0.0077351555, -0.028162204, -0.11196239, -0.09236244, 0.055049483, 0.05579075, -0.005223511, -0.0435036, -0.04896749, -0.03345477, 0.0038895514, 0.017122723, -0.07208417, 0.016996462, 0.0065576, 0.025109183, 0.01175039, 0.03366881, 0.07141689, -0.014054037, 0.016879817, 0.031477056, 0.03632796, 0.06395024, -0.04220069, 0.0062176483, -0.022527335, -0.025984455, -0.0647694, 0.054601815, -0.015159034, 0.014657266, 0.04409256, -0.015946683, 0.011887132, 0.026414476, 0.020927155, -0.016512435, 0.09359048, 0.029739358, -0.066180184, 0.082244694, 0.0007292507, -0.06282271, 0.035395358, -0.100961864, 0.014836456, 0.11625059, -0.023679407, -0.013240734, 0.019296095, -0.028371686, 0.016569745, 0.008198354, -0.002588122, -0.061931096, -0.019892568, -0.011799377, 0.016310172, -0.0044856467, -0.0267413, -0.005191055, 0.04924748, -0.0053692097, -0.03609329, 0.049340405, 0.111295922, 0.069036305, 0.0036290872, -0.0040835966, 0.0035751562, -0.035198208, -0.0015323451, 0.030191373, 0.0015703973, -0.018142749, -0.011257919, -0.00057657144, -0.053825088, 0.01760392, -0.001581838, 0.02007053, -0.05818865, 0.04108587, -0.028711911, 0.03198221, 0.005932087, -0.01670024, 0.0047082426, 0.025187634, -0.0069206334, -0.020081813, 0.0058442047, -0.0054093692, -0.07816217, -0.04283457, 0.05345854, -0.018779771, 0.056370307, 0.057341665, -0.012000827, -0.032532148, 0.01690849, 0.06947271, -0.017020883, 0.014368475, -0.07444708, -0.013201608, -0.003327803, -0.0357886, -0.014834566, -0.111255137 ]
}
```

### Response
```
{
    "distance": 0.173493515728975,
    "model_version": 2,
    "smartcontract": "0x0001234"
}
```
Status 200

## DEL /delete/\<smartcontract>

Delete \<smartcontract>

### Response
```
[]
```
Status 200