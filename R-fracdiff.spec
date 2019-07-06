#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fracdiff
Version  : 1.4.2
Release  : 12
URL      : https://cran.r-project.org/src/contrib/fracdiff_1.4-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fracdiff_1.4-2.tar.gz
Summary  : Fractionally differenced ARIMA aka ARFIMA(p,d,q) models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fracdiff-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
fracdiff Maximum likelihood estimation of the parameters of a fractionally
differenced ARIMA (p,d,q) model. For long-memory dependence in
time series. (Haslett and Raftery, Applied Statistics 38, 1989, 1-50).

%package lib
Summary: lib components for the R-fracdiff package.
Group: Libraries

%description lib
lib components for the R-fracdiff package.


%prep
%setup -q -c -n fracdiff

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552922545

%install
export SOURCE_DATE_EPOCH=1552922545
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fracdiff
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fracdiff
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fracdiff
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  fracdiff || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fracdiff/DESCRIPTION
/usr/lib64/R/library/fracdiff/INDEX
/usr/lib64/R/library/fracdiff/Meta/Rd.rds
/usr/lib64/R/library/fracdiff/Meta/features.rds
/usr/lib64/R/library/fracdiff/Meta/hsearch.rds
/usr/lib64/R/library/fracdiff/Meta/links.rds
/usr/lib64/R/library/fracdiff/Meta/nsInfo.rds
/usr/lib64/R/library/fracdiff/Meta/package.rds
/usr/lib64/R/library/fracdiff/NAMESPACE
/usr/lib64/R/library/fracdiff/R/fracdiff
/usr/lib64/R/library/fracdiff/R/fracdiff.rdb
/usr/lib64/R/library/fracdiff/R/fracdiff.rdx
/usr/lib64/R/library/fracdiff/help/AnIndex
/usr/lib64/R/library/fracdiff/help/aliases.rds
/usr/lib64/R/library/fracdiff/help/fracdiff.rdb
/usr/lib64/R/library/fracdiff/help/fracdiff.rdx
/usr/lib64/R/library/fracdiff/help/paths.rds
/usr/lib64/R/library/fracdiff/html/00Index.html
/usr/lib64/R/library/fracdiff/html/R.css
/usr/lib64/R/library/fracdiff/tests/Valderio-ex.R
/usr/lib64/R/library/fracdiff/tests/Valderio-ex.Rout.save
/usr/lib64/R/library/fracdiff/tests/ex-Vinod.R
/usr/lib64/R/library/fracdiff/tests/ex.R
/usr/lib64/R/library/fracdiff/tests/ex.Rout-32b
/usr/lib64/R/library/fracdiff/tests/ex.Rout-64b
/usr/lib64/R/library/fracdiff/tests/ex.Rout.save
/usr/lib64/R/library/fracdiff/tests/sim-2.R
/usr/lib64/R/library/fracdiff/tests/sim-ex.R
/usr/lib64/R/library/fracdiff/tests/sim-ex.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fracdiff/libs/fracdiff.so
/usr/lib64/R/library/fracdiff/libs/fracdiff.so.avx2
/usr/lib64/R/library/fracdiff/libs/fracdiff.so.avx512
