Shader "Hidden/FRTE/PhotoTransform"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        // No culling or depth
        Cull Off ZWrite Off ZTest Always

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

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = v.uv;
                return o;
            }

            sampler2D _MainTex;
            float4 _TransformRow0; // (m00, m01, m02, 0)
            float4 _TransformRow1; // (m10, m11, m12, 0)

            fixed4 frag (v2f i) : SV_Target
            {
                // Calculate source UV using the affine transformation matrix
                float3 outputUV = float3(i.uv, 1.0);
                float2 sourceUV;
                sourceUV.x = dot(_TransformRow0.xyz, outputUV);
                sourceUV.y = dot(_TransformRow1.xyz, outputUV);

                // Sample texture with clamp to border (handled by shader clamp or transparent color if out of bounds)
                if (sourceUV.x < 0.0 || sourceUV.x > 1.0 || sourceUV.y < 0.0 || sourceUV.y > 1.0)
                {
                    return fixed4(0, 0, 0, 0); // Out of bounds pixels are transparent
                }

                return tex2D(_MainTex, sourceUV);
            }
            ENDCG
        }
    }
}
