#ifndef IMAGE_PROVIDER_H_
#define IMAGE_PROVIDER_H_


#ifdef WITH_INTEL_HLS
	#include "HLS/stdio.h"
#else
	#include <stdio.h>
	#define component
#endif // WITH_INTEL_HLS

void image_provider();

void show_image(const char* relative_path);

#endif // IMAGE_PROVIDER_H_