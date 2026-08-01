Shader "FRTE/DeformableJelly"
{
    Properties
    {
        _MainTex ("Jelly Texture", 2D) = "white" {}
        [Header("Ripple Refraction")]
        _RippleCenter ("Ripple Center (UV)", Vector) = (0.5, 0.5, 0, 0)
        _RippleParams ("Ripple Params (Amp, Freq, Speed, Decay)", Vector) = (0, 10, 5, 2)
    }
    SubShader
    {
        Tags { "Queue"="Geometry" "RenderType"="Opaque" }
        LOD 100

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"

            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct v2f
            {
                float2 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;
            float4 _MainTex_ST;
            float4 _RippleCenter;
            float4 _RippleParams; // x: Amplitude, y: Frequency, z: Speed, w: Decay

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = TRANSFORM_TEX(v.uv, _MainTex);
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                float2 center = _RippleCenter.xy;
                float amp = _RippleParams.x;
                float freq = _RippleParams.y;
                float speed = _RippleParams.z;
                float decay = _RippleParams.w;

                // Calculate displacement vector
                float2 toCenter = i.uv - center;
                float dist = length(toCenter);

                float2 offsetUV = i.uv;

                if (dist > 0.0001 && amp > 0.00001)
                {
                    // Refractive wave equation: sin(d * freq - t * speed) * exp(-d * decay) * amp
                    float wave = sin(dist * freq - _Time.y * speed) * exp(-dist * decay) * amp;
                    offsetUV += normalize(toCenter) * wave;
                }

                // Sample texture with clamped coordinates to prevent border artifacts
                fixed4 col = tex2D(_MainTex, saturate(offsetUV));
                return col;
            }
            ENDCG
        }
    }
}
