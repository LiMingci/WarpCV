#pragma once
#include <opencv/cv.h>
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>

namespace nld {
enum DIFFUSIVITY_TYPE
{
	PM_G1 = 0,
	PM_G2 = 1,
	WEICKERT = 2,
	CHARBONNIER = 3
};

class CV_EXPORTS_W_SIMPLE CcADFConfig
{
public:
	CV_PROP_RW float _ttime;
	CV_PROP_RW int _diffusivity;   ///< Diffusivity type
	CV_PROP_RW float _tmax;
	CV_PROP_RW float _soffset;

	CV_WRAP CcADFConfig(
		float ttime = 2.0f,
		int diffusivity = PM_G2,
		float tmax = 0.25,
		float soffset = 1.6f) 
		: _ttime(ttime), _diffusivity(diffusivity), _tmax(tmax), _soffset(soffset)
	{
		//
	}

};

class CV_EXPORTS_W CcADF
{
public:
	CV_WRAP CcADF(const CcADFConfig& config = CcADFConfig());
	~CcADF();

	CV_WRAP bool AnisotropicDiffusionFilter(const cv::InputArray& srcMat, cv::OutputArray& dstMat);

private:
	bool AnisotropicDiffusionFilterSingle(const cv::Mat& srcMat, cv::Mat& dstMat);

	bool AnisotropicDiffusionFilterMutil(const cv::Mat& srcMat, cv::Mat& dstMat);

private:
	CcADFConfig _config;

};

}