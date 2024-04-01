## Keşifsel Veri Analizi (EDA)
Exploratory Data Analysis - EDA, veri bilimi ve istatistikte kullanılan önemli bir adımdır. EDA, bir veri setini anlamak, içindeki yapıları keşfetmek, özelliklerini tanımlamak ve veri hakkında fikir sahibi olmak için yapılan bir dizi yöntem ve tekniktir. Temel amacı, veri setindeki ana özellikleri, ilişkileri ve desenleri ortaya çıkarmak ve veri hakkında ön bilgi sahibi olmaktır.

Bu Python scripti, veri setinizin karmaşıklığını anlamak ve içerdiği bilgileri ortaya çıkarmak için tasarlanmış bir dizi fonksiyon içermektedir. Bu fonksiyonlar, veri setinizdeki değişkenlerin türlerini belirlemekten başlayarak, kategorik ve sayısal değişkenlerin ayrıntılı özetlerini çıkarmak, görselleştirmeler oluşturmak ve hedef değişken ile diğer değişkenler arasındaki ilişkileri keşfetmek için geliştirilmiştir.

### Fonksiyonlar ve Açıklamaları
#### grap_col_names(dataframe, cat_th=10, car_th=20) : Bu fonksiyon, veri setinizdeki değişkenleri kategorik, sayısal ve kategorik ama kardinal olup olmadığının ayrımını yapar

- cat_th: Kategorik olarak düşünülen ancak numerik görünen değişkenler için sınıf eşik değeri

- car_th: Kategorik fakat kardinal olarak düşünülen değişkenler için sınıf eşik değeri

### Fonksiyon çıktısı olarak:

- cat_cols: Kategorik değişken isimleri

- num_cols: Sayısal değişken isimleri

- cat_car: Kategorik görünümlü kardinal değişkenlerin listesi

#### cat_summary(dataframe, col_name) : Bu fonksiyon, veri setinizdeki belirli bir kategorik değişkenin değerlerinin sayısını ve yüzdesini görüntüler.

- dataframe: İncelenen veri seti

- col_name: İncelenen kategorik değişkenin adı

#### num_summary(dataframe, numerical_col, plot=False) : Bu fonksiyon, veri setinizdeki belirli bir sayısal değişkenin istatistik özetini ve isteğe bağlı olarak histogramını görüntüler.

- numerical_col: İncelenen sayısal değişkenin adı
  
- plot: Histogramı görüntülemek için bool değeri
  
#### cat_Summary(dataframe, col_name, plot=False) : Bu fonksiyon, veri setinizdeki belirli bir kategorik değişkenin değerlerinin sayısını ve yüzdesini görüntüler. Ayrıca isteğe bağlı olarak bu dağılımı bir çubuk grafik ile gösterir.

#### target_summary_with_cat(dataframe, target, categorical_col) : Bu fonksiyon, hedef değişkeninizle belirli bir kategorik değişken arasındaki ilişkiyi incelemek için kullanılır. Hedef değişkenin ortalamasını kategorik değişkenlere göre gruplayarak gösterir.

#### target_summary_with_num(dataframe, target, numerical_col) : Bu fonksiyon, hedef değişkeninizle belirli bir sayısal değişken arasındaki ilişkiyi incelemek için kullanılır. Hedef değişkenin ortalamasını sayısal değişkenlere göre gruplayarak gösterir.

#### high_correlated_cols(dataframe, plot=False, corr_th=0.90) : Bu fonksiyon, veri setinizdeki yüksek korelasyonlu sütunları belirlemek için kullanılır. Belirtilen eşik değerinden yüksek korelasyona sahip sütunları bulur ve isteğe bağlı olarak bir ısı haritası ile gösterir.


### Veri Seti
Bu script, Titanic veri seti üzerinde örnekler ile çalışmaktadır. Sonrasında ise breast_cancer veri seti ile korelasyon analizi yapılmaktadır. Ancak, istediğiniz başka bir veri seti üzerinde de kullanabilirsiniz.

### ÖNEMLİ NOT!!
Korelasyon analizi her veri seti için uygulanan bir yöntem değildir. Verinin yapısına ve amacına bağlı olarak yapmanız gereken işlemler değişiklik göstermektedir. 
