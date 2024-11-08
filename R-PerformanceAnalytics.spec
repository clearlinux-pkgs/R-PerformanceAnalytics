#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-PerformanceAnalytics
Version  : 2.0.4
Release  : 61
URL      : https://cran.r-project.org/src/contrib/PerformanceAnalytics_2.0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/PerformanceAnalytics_2.0.4.tar.gz
Summary  : Econometric Tools for Performance and Risk Analysis
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-PerformanceAnalytics-lib = %{version}-%{release}
Requires: R-quadprog
Requires: R-xts
Requires: R-zoo
BuildRequires : R-quadprog
BuildRequires : R-xts
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
analysis. In addition to standard risk and performance metrics, this 
    package aims to aid practitioners and researchers in utilizing the latest
    research in analysis of non-normal return streams.  In general, it is most 
    tested on return (rather than price) data on a regular scale, but most 
    functions will work with irregular return data as well, and increasing
    numbers of functions will work with P&L or price data where possible.

%package lib
Summary: lib components for the R-PerformanceAnalytics package.
Group: Libraries

%description lib
lib components for the R-PerformanceAnalytics package.


%prep
%setup -q -c -n PerformanceAnalytics
cd %{_builddir}/PerformanceAnalytics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641072630

%install
export SOURCE_DATE_EPOCH=1641072630
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PerformanceAnalytics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PerformanceAnalytics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PerformanceAnalytics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc PerformanceAnalytics || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/PerformanceAnalytics/DESCRIPTION
/usr/lib64/R/library/PerformanceAnalytics/INDEX
/usr/lib64/R/library/PerformanceAnalytics/Meta/Rd.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/data.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/features.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/hsearch.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/links.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/nsInfo.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/package.rds
/usr/lib64/R/library/PerformanceAnalytics/Meta/vignette.rds
/usr/lib64/R/library/PerformanceAnalytics/NAMESPACE
/usr/lib64/R/library/PerformanceAnalytics/NEWS
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics.rdb
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics.rdx
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rdb
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rds
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rdx
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.R
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-Bacon.R
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-Bacon.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-Bacon.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-charts.R
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-charts.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/PA-charts.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/PA_StandardErrors.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/PA_StandardErrors.pdf.asis
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsChartsPresentation-Meielisalp-2007.R
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsChartsPresentation-Meielisalp-2007.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsChartsPresentation-Meielisalp-2007.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsPresentation-UseR-2007.R
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsPresentation-UseR-2007.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/PerformanceAnalyticsPresentation-UseR-2007.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/index.html
/usr/lib64/R/library/PerformanceAnalytics/doc/portfolio_returns.R
/usr/lib64/R/library/PerformanceAnalytics/doc/portfolio_returns.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/portfolio_returns.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/textplotPresentation-CRUG-2011.R
/usr/lib64/R/library/PerformanceAnalytics/doc/textplotPresentation-CRUG-2011.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/textplotPresentation-CRUG-2011.pdf
/usr/lib64/R/library/PerformanceAnalytics/help/AnIndex
/usr/lib64/R/library/PerformanceAnalytics/help/PerformanceAnalytics.rdb
/usr/lib64/R/library/PerformanceAnalytics/help/PerformanceAnalytics.rdx
/usr/lib64/R/library/PerformanceAnalytics/help/aliases.rds
/usr/lib64/R/library/PerformanceAnalytics/help/paths.rds
/usr/lib64/R/library/PerformanceAnalytics/html/00Index.html
/usr/lib64/R/library/PerformanceAnalytics/html/R.css
/usr/lib64/R/library/PerformanceAnalytics/tests/Examples/PerformanceAnalytics-Ex.Rout.save
/usr/lib64/R/library/PerformanceAnalytics/tests/tinytest.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_PerformanceAnalytics.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_Return.portfolio.geometric.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_to.period.contributions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so
/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so.avx2
/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so.avx512
