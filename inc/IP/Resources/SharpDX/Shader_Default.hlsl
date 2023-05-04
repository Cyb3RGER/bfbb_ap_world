﻿
cbuffer data :register(b0)
{
	float4x4 worldViewProj;
};

struct VS_IN
{
	float4 position : POSITION;
	float4 color : COLOR;
	float2 texcoord : TEXCOORD;
};

struct PS_IN
{
	float4 position : SV_POSITION;
	float4 color : COLOR;
	float2 texcoord : TEXCOORD;
};

//texture
Texture2D textureMap;
SamplerState textureSampler
{
	Filter = ANISOTROPIC;
	AddressU = Wrap;
	AddressV = Wrap;
};

PS_IN VS(VS_IN input)
{
	PS_IN output = (PS_IN)0;

	output.position = mul(worldViewProj, input.position);
	output.texcoord = input.texcoord;
	output.color = input.color;

	return output;
}

float4 PS(PS_IN input) : SV_Target
{
	return textureMap.Sample(textureSampler, input.texcoord) * input.color;
}