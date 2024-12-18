#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-PerformanceAnalytics
Version  : 2.0.8
Release  : 62
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/PerformanceAnalytics_2.0.8.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/PerformanceAnalytics_2.0.8.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n PerformanceAnalytics
pushd ..
cp -a PerformanceAnalytics buildavx2
popd
pushd ..
cp -a PerformanceAnalytics buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1733821243

%install
export SOURCE_DATE_EPOCH=1733821243
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics.rdb
/usr/lib64/R/library/PerformanceAnalytics/R/PerformanceAnalytics.rdx
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rdb
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rds
/usr/lib64/R/library/PerformanceAnalytics/data/Rdata.rdx
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.R
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.Rnw
/usr/lib64/R/library/PerformanceAnalytics/doc/EstimationComoments.pdf
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
/usr/lib64/R/library/PerformanceAnalytics/doc/textplotPresentation-CRUG-2011.pdf
/usr/lib64/R/library/PerformanceAnalytics/doc/textplotPresentation-CRUG-2011.pdf.asis
/usr/lib64/R/library/PerformanceAnalytics/help/AnIndex
/usr/lib64/R/library/PerformanceAnalytics/help/PerformanceAnalytics.rdb
/usr/lib64/R/library/PerformanceAnalytics/help/PerformanceAnalytics.rdx
/usr/lib64/R/library/PerformanceAnalytics/help/aliases.rds
/usr/lib64/R/library/PerformanceAnalytics/help/paths.rds
/usr/lib64/R/library/PerformanceAnalytics/html/00Index.html
/usr/lib64/R/library/PerformanceAnalytics/html/R.css
/usr/lib64/R/library/PerformanceAnalytics/tests/tinytest.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_CAPM.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_PerformanceAnalytics.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_Return.portfolio.arithmetic.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_Return.portfolio.geometric.R
/usr/lib64/R/library/PerformanceAnalytics/tinytest/test_to.period.contributions.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so
/V4/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so
/usr/lib64/R/library/PerformanceAnalytics/libs/PerformanceAnalytics.so
